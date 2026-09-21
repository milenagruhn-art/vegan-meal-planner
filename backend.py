"""Small local backend for NutriCraft's Gemini requests.

Run with GEMINI_API_KEY set in the environment:
    $env:GEMINI_API_KEY = "..."
    python backend.py
"""

import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HOST = os.getenv("NUTRICRAFT_HOST", "127.0.0.1")
PORT = int(os.getenv("NUTRICRAFT_PORT", "8000"))
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
ROOT = Path(__file__).resolve().parent
MAX_REQUESTS_PER_MINUTE = 5
MAX_BODY_BYTES = 64 * 1024
request_log = {}
request_log_lock = threading.Lock()

PROMPT = """Erstelle einen 7-Tage-Ernährungsplan (Montag bis Sonntag) für 2 Personen.
Mahlzeiten: Frühstück, Mittagessen, Abendessen, Snack.
Regeln: Keine rohen Tomaten. Hohe Bioverfügbarkeit (Eisen, Vitamin C).
Berücksichtige die Vorräte, die bereits zu Hause sind, und plane Zutaten, die bald verbraucht werden müssen, bevorzugt ein.
Antworte ausschließlich im JSON-Format mit dieser Struktur:
{
  "Montag": {
    "Frühstück": {"name": "...", "device": "...", "bio": "...", "calories": 400, "protein": 20, "ingredients": [{"item": "...", "amount": 100, "unit": "g"}], "instructions": "..."},
    "Mittagessen": {"name": "...", "device": "...", "bio": "...", "calories": 500, "protein": 25, "ingredients": [{"item": "...", "amount": 100, "unit": "g"}], "instructions": "..."},
    "Abendessen": {"name": "...", "device": "...", "bio": "...", "calories": 500, "protein": 25, "ingredients": [{"item": "...", "amount": 100, "unit": "g"}], "instructions": "..."},
    "Snack": {"name": "...", "device": "...", "bio": "...", "calories": 200, "protein": 10, "ingredients": [{"item": "...", "amount": 50, "unit": "g"}], "instructions": "..."}
  }
}
Ergänze die sechs übrigen Tage mit derselben Struktur."""

MEAL_PROMPT = """Erstelle genau ein Rezept für {meal_type} am {day} für 2 Personen.
Keine rohen Tomaten. Hohe Bioverfügbarkeit (Eisen, Vitamin C).
Bereits vorhanden: {pantry}.
Muss bevorzugt verbraucht werden: {use_soon}.
Antworte ausschließlich als JSON mit den Feldern name, device, bio, calories, protein, ingredients und instructions."""


def preference_rules(preferences):
    preferences = preferences if isinstance(preferences, dict) else {}
    dietary_forms = {
        "vegan": "Vegan: keinerlei tierische Produkte.",
        "vegetarisch": "Vegetarisch: kein Fleisch, kein Fisch und keine Meeresfrüchte.",
        "allesesser": "Allesesser: Es dürfen pflanzliche und tierische Zutaten verwendet werden.",
    }
    dietary_form = str(preferences.get("dietaryForm", "vegan")).lower()
    exclusions = preferences.get("exclusions", [])
    exclusions = [str(item).strip()[:80] for item in exclusions[:12] if str(item).strip()] if isinstance(exclusions, list) else []
    cuisine_preferences = str(preferences.get("cuisinePreferences", "")).strip()[:500]
    additional_preferences = str(preferences.get("additionalPreferences", "")).strip()[:1000]
    rules = [
        "\nVERBINDLICHE PERSONALISIERTE REGELN (niemals ignorieren):",
        dietary_forms.get(dietary_form, dietary_forms["vegan"]),
    ]
    if exclusions:
        rules.append("Diese Zutaten vollständig vermeiden, auch in Saucen, Brühen, Gewürzmischungen und Fertigprodukten: " + ", ".join(exclusions) + ".")
    if cuisine_preferences:
        rules.append("Küchenrichtungen und Geschmackswünsche strikt beachten: " + cuisine_preferences)
    if additional_preferences:
        rules.append("Weitere individuelle Wünsche und Vermeidungen strikt beachten: " + additional_preferences)
    rules.append("Bei Konflikten haben diese personalisierten Regeln Vorrang vor allgemeinen Rezeptideen. Prüfe jedes Gericht und jede Zutat vor der Ausgabe.")
    return "\n".join(rules)


class NutriCraftHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/health":
            self.send_json(200, {"ok": True})
            return
        if self.path in ("/", "/index.html"):
            self.serve_index()
            return
        self.send_json(404, {"error": "Nicht gefunden."})

    def do_POST(self):
        if self.path not in ("/api/generate", "/api/generate-meal"):
            self.send_json(404, {"error": "Nicht gefunden."})
            return
        if not self.is_allowed():
            self.send_json(429, {"error": "Zu viele Anfragen. Bitte später erneut versuchen."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY_BYTES:
            self.send_json(413, {"error": "Die Anfrage ist zu groß oder ungültig."})
            return
        api_key = os.getenv("GEMINI_API_KEY", "").strip()
        if not api_key:
            self.send_json(503, {"error": "GEMINI_API_KEY ist auf dem Server nicht gesetzt."})
            return

        try:
            request_data = json.loads(self.rfile.read(length))
        except (ValueError, json.JSONDecodeError):
            request_data = {}
        if not isinstance(request_data, dict):
            self.send_json(400, {"error": "Die Anfrage muss ein JSON-Objekt sein."})
            return
        if self.path == "/api/generate-meal":
            day = str(request_data.get("day", ""))
            meal_type = str(request_data.get("mealType", ""))
            if day not in {"Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"} or meal_type not in {"Frühstück", "Mittagessen", "Abendessen", "Snack"}:
                self.send_json(400, {"error": "Tag und Mahlzeit fehlen."})
                return
            preference_prompt = preference_rules(request_data.get("preferences"))
            prompt = MEAL_PROMPT.format(
                day=day,
                meal_type=meal_type,
                pantry=", ".join(str(item)[:80] for item in request_data.get("pantry", [])[:30]) if isinstance(request_data.get("pantry", []), list) else "keine",
                use_soon=", ".join(str(item)[:80] for item in request_data.get("useSoon", [])[:30]) if isinstance(request_data.get("useSoon", []), list) else "keine",
            )
        else:
            preference_prompt = preference_rules(request_data.get("preferences"))
            pantry = request_data.get("pantry", [])
            use_soon = request_data.get("useSoon", [])
            pantry = ", ".join(str(item)[:80] for item in pantry[:30]) if isinstance(pantry, list) else "keine"
            use_soon = ", ".join(str(item)[:80] for item in use_soon[:30]) if isinstance(use_soon, list) else "keine"
            prompt = PROMPT + f"\nBereits vorhanden: {pantry or 'keine'}.\nMuss verbraucht werden: {use_soon or 'keine'}."

        request = Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
            data=json.dumps({
                "systemInstruction": {"parts": [{"text": preference_prompt}]},
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"responseMimeType": "application/json"},
            }).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
            method="POST",
        )
        try:
            with urlopen(request, timeout=45) as response:
                upstream = json.loads(response.read().decode("utf-8"))
            raw_text = upstream["candidates"][0]["content"]["parts"][0]["text"]
            plan = json.loads(raw_text)
            self.send_json(200, plan)
        except HTTPError as error:
            status = error.code if error.code in (400, 401, 403, 429) else 502
            try:
                upstream_error = json.loads(error.read().decode("utf-8"))
                detail = upstream_error.get("error", {}).get("message", "")
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                detail = ""
            detail = detail.replace(api_key, "[geschützt]") if detail else ""
            if error.code in (401, 403):
                message = "Gemini-Key ist ungültig oder für dieses Modell nicht freigeschaltet."
            elif error.code == 429:
                message = "Gemini-Limit erreicht. Bitte später erneut versuchen."
            elif error.code == 400:
                message = "Gemini hat die Anfrage abgelehnt. Modell oder Anfrage prüfen."
            else:
                message = "Gemini-Anfrage fehlgeschlagen."
            print(f"Gemini HTTP-Fehler: {error.code} ({error.reason}) {detail}")
            suffix = f" Details: {detail}" if detail else ""
            self.send_json(status, {"error": f"{message} (HTTP {error.code}).{suffix}"})
        except URLError as error:
            print(f"Netzwerkfehler zu Gemini: {error.reason}")
            self.send_json(502, {"error": "Gemini ist nicht erreichbar. Prüfe deine Internetverbindung oder Firewall."})
        except TimeoutError:
            print("Zeitüberschreitung bei der Gemini-Anfrage")
            self.send_json(504, {"error": "Gemini antwortet zu langsam. Bitte erneut versuchen."})
        except (KeyError, IndexError, json.JSONDecodeError):
            print("Ungültige Antwort von Gemini")
            self.send_json(502, {"error": "Gemini hat keine gültige JSON-Antwort geliefert."})

    def is_allowed(self):
        now = time.monotonic()
        client = self.client_address[0]
        with request_log_lock:
            recent = [stamp for stamp in request_log.get(client, []) if now - stamp < 60]
            if len(recent) >= MAX_REQUESTS_PER_MINUTE:
                request_log[client] = recent
                return False
            recent.append(now)
            request_log[client] = recent
            return True

    def serve_index(self):
        try:
            content = (ROOT / "index.html").read_bytes()
        except OSError:
            self.send_json(500, {"error": "index.html konnte nicht gelesen werden."})
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_security_headers()
        self.end_headers()
        self.wfile.write(content)

    def send_json(self, status, payload):
        content = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_security_headers()
        self.end_headers()
        self.wfile.write(content)

    def send_security_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Security-Policy", "default-src 'self' https://cdn.jsdelivr.net; connect-src 'self'; script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; style-src 'self' 'unsafe-inline'")

    def log_message(self, format, *args):
        if self.path != "/api/health":
            super().log_message(format, *args)


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), NutriCraftHandler)
    print(f"NutriCraft läuft auf http://{HOST}:{PORT}")
    print("GEMINI_API_KEY ist gesetzt:", bool(os.getenv("GEMINI_API_KEY")))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer beendet.")
    finally:
        server.server_close()
