# NutriCraft sicher starten

Das Frontend ruft Gemini nicht mehr direkt auf. Der API-Key bleibt ausschließlich als Umgebungsvariable im Backend.
Das Backend verwendet standardmäßig `gemini-3.6-flash`, das für diesen Key verfügbar ist. `gemini-1.5-flash` und `gemini-2.5-flash` waren für den bisherigen Aufruf nicht verfügbar.

## Lokal unter Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY = "DEIN_GEMINI_KEY"
python backend.py
```

Ein anderes verfügbares Modell kannst du vor dem Start setzen:

```powershell
$env:GEMINI_MODEL = "gemini-3.6-flash"
```

Danach im Browser öffnen: http://127.0.0.1:8000

Der Server bindet standardmäßig nur an `127.0.0.1`. Dadurch ist er aus dem Netzwerk nicht erreichbar. Der Endpoint akzeptiert höchstens fünf Generierungen pro Minute je IP-Adresse.

## Wichtig für Veröffentlichung

Nicht mit `NUTRICRAFT_HOST=0.0.0.0` ins Internet stellen. Für einen öffentlichen Betrieb brauchst du HTTPS, einen Reverse Proxy und zusätzliche Benutzer-Authentifizierung. Der Gemini-Key sollte außerdem nur als Secret deines Hosting-Anbieters hinterlegt werden.

Den alten Key aus dem Browser entfernen:

```js
localStorage.removeItem('nutri_gemini_key')
```
