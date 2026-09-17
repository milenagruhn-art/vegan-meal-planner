import random
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="NutriCraft Vegan App",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    .main { background-color: #f9fbe7; }
    .stButton>button { border-radius: 8px; font-weight: bold; }
    .recipe-card { background-color: #ffffff; padding: 20px; border-radius: 12px; border-left: 5px solid #2e7d32; box-shadow: 0 2px 5px rgba(0,0,0,0.05); margin-bottom: 20px; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- REZEPT-DATENBANK ---
INITIAL_RECIPE_POOL = {
    "Frühstück": [
        {
            "name": "Matcha-Chia-Pudding mit Mango & Hanfsamen",
            "device": "Kühlschrank",
            "ingredients": [
                {"item": "Chiasamen", "amount": 60, "unit": "g"},
                {"item": "Pflanzenmilch", "amount": 400, "unit": "ml"},
                {"item": "Matcha-Pulver", "amount": 2, "unit": "TL"},
                {"item": "Geschälte Hanfsamen", "amount": 30, "unit": "g"},
                {"item": "Reife Mango", "amount": 1, "unit": "Stück"},
            ],
            "instructions": "Chiasamen, Matcha und Pflanzenmilch verrühren und über Nacht im Kühlschrank quellen lassen. Vor dem Servieren mit geschälten Hanfsamen und frischen Mangowürfeln toppen.",
        },
        {
            "name": "Overnight Golden-Milk Oats mit Kürbiskernen",
            "device": "Kühlschrank",
            "ingredients": [
                {"item": "Zarte Haferflocken", "amount": 160, "unit": "g"},
                {"item": "Pflanzenmilch", "amount": 400, "unit": "ml"},
                {"item": "Kurkuma & Prise Pfeffer", "amount": 1, "unit": "TL"},
                {"item": "Kürbiskerne", "amount": 40, "unit": "g"},
            ],
            "instructions": "Haferflocken mit Kurkuma, einer Prise schwarzem Pfeffer und Pflanzenmilch mischen. Über Nacht abgedeckt kaltstellen. Morgens mit gerösteten Kürbiskernen garnieren.",
        },
        {
            "name": "Fancy Tofu-Scramble Toast mit Avocado & Schnittlauch",
            "device": "Herd",
            "ingredients": [
                {"item": "Naturtofu", "amount": 300, "unit": "g"},
                {"item": "Kala Namak Salz", "amount": 1, "unit": "TL"},
                {"item": "Kurkuma", "amount": 0.5, "unit": "TL"},
                {"item": "Avocado", "amount": 2, "unit": "Stück"},
                {"item": "Sauerteigbrot", "amount": 4, "unit": "Scheiben"},
            ],
            "instructions": "Tofu mit den Händen zerkrümeln und in etwas Öl anbraten. Kurkuma und Kala Namak dazugeben. Sauerteigbrot anrösten, mit zerdrückter Avocado bestreichen und den Rühreitofu darauf verteilen.",
        },
    ],
    "Mittagessen": [
        {
            "name": "Japanische Tofu-Katsu Bowl & Miso-Dressing",
            "device": "Airfryer & Herd",
            "ingredients": [
                {"item": "Naturtofu (fest)", "amount": 400, "unit": "g"},
                {"item": "Sushi-Reis", "amount": 200, "unit": "g"},
                {"item": "Panko-Panermehl", "amount": 80, "unit": "g"},
                {"item": "Brokkoli", "amount": 1, "unit": "Kopf"},
                {"item": "Edamame", "amount": 150, "unit": "g"},
            ],
            "instructions": "Reis kochen. Tofu in Scheiben schneiden, in Mehl-Wasser-Gemisch wenden und in Panko panieren. Bei 200°C 12 Min im Airfryer knusprig backen. Brokkoli und Edamame dämpfen und alles in einer Bowl anrichten.",
        },
        {
            "name": "Linsensalat mit Süßkartoffeln aus dem Airfryer",
            "device": "Airfryer & Herd",
            "ingredients": [
                {"item": "Braune Linsen", "amount": 200, "unit": "g"},
                {"item": "Süßkartoffeln", "amount": 2, "unit": "Stück"},
                {"item": "Walnüsse", "amount": 50, "unit": "g"},
                {"item": "Feldsalat", "amount": 150, "unit": "g"},
            ],
            "instructions": "Linsen nach Packung kochen. Süßkartoffeln würfeln und im Airfryer bei 190°C ca. 15 Minuten rrösten. Zusammen mit Feldsalat, Walnüssen und einem Zitronen-Dressing vermengen.",
        },
    ],
    "Abendessen": [
        {
            "name": "Cremiges Dal Makhani mit Ofen-Blumenkohl",
            "device": "Herd & Backofen",
            "ingredients": [
                {"item": "Schwarze Linsen (Beluga)", "amount": 350, "unit": "g"},
                {"item": "Kokosmilch (vollfett)", "amount": 400, "unit": "ml"},
                {"item": "Passierte Tomaten (Sauce)", "amount": 400, "unit": "ml"},
                {"item": "Garam Masala & Kurkuma", "amount": 2, "unit": "EL"},
                {"item": "Blumenkohl", "amount": 1, "unit": "Kopf"},
            ],
            "instructions": "Linsen weichkochen. Gewürze in etwas Öl anbraten, mit passierten Tomaten und Kokosmilch ablöschen, Linsen zugeben und sanft köcheln lassen. Blumenkohl im Ofen rösten und als Topping servieren.",
        },
        {
            "name": "Airfryer Tempeh-Tacos mit Mango-Salsa",
            "device": "Airfryer",
            "ingredients": [
                {"item": "Tempeh", "amount": 300, "unit": "g"},
                {"item": "Kleine Mais-Tacos", "amount": 8, "unit": "Stück"},
                {"item": "Reife Mango", "amount": 1, "unit": "Stück"},
                {"item": "Avocado", "amount": 2, "unit": "Stück"},
                {"item": "Rotkohl", "amount": 200, "unit": "g"},
            ],
            "instructions": "Tempeh würfeln, marinieren und im Airfryer 10 Min kross braten. Mango, Avocado und Rotkohl klein schneiden. Tacos erwärmen und nach Wunsch belegen.",
        },
    ],
    "Snack": [
        {
            "name": "Airfryer Würzige Grünkohlchips & Ingwer-Shot",
            "device": "Airfryer & Entsafter",
            "ingredients": [
                {"item": "Frischer Grünkohl", "amount": 200, "unit": "g"},
                {"item": "Hefeflocken", "amount": 3, "unit": "EL"},
                {"item": "Ingwer & Kurkuma-Wurzel", "amount": 100, "unit": "g"},
            ],
            "instructions": "Grünkohl waschen, trocknen, mit etwas Öl und Hefeflocken einreiben und bei 160°C ca. 5 Min im Airfryer kross backen. Ingwer und Kurkuma durch den Entsafter jagen.",
        },
        {
            "name": "Airfryer Kichererbsen mit Smoke-Paprika",
            "device": "Airfryer",
            "ingredients": [
                {"item": "Kichererbsen (Dose)", "amount": 1, "unit": "Dose"},
                {"item": "Rauchpaprika", "amount": 1, "unit": "EL"},
            ],
            "instructions": "Kichererbsen abspülen, gründlich abtrocknen, mit Öl und Rauchpaprika würzen. Im Airfryer bei 200°C 12-15 Minuten knusprig rösten.",
        },
    ],
}

DAYS = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
]
MEAL_TYPES = ["Frühstück", "Mittagessen", "Abendessen", "Snack"]

# --- SESSION STATE INITIALISIERUNG ---
if "recipe_pool" not in st.session_state:
    st.session_state.recipe_pool = INITIAL_RECIPE_POOL

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "exclusions" not in st.session_state:
    st.session_state.exclusions = ["Tomaten"]  # Default Ausschluss

# Generator-Logik mit Berücksichtigung der Ausschlüsse
def filter_recipe(recipe, exclusions):
    """Prüft, ob ein Rezept eine ausgeschlossene Zutat enthält"""
    for ing in recipe.get("ingredients", []):
        for exc in exclusions:
            if exc.lower() in ing["item"].lower():
                return False
    return True


def generate_week():
    plan = {}
    exclusions = st.session_state.exclusions

    for day in DAYS:
        plan[day] = {}
        for m_type in MEAL_TYPES:
            # Di/Mi Mittagessen ist Meal Prep vom Mo-Abendessen
            if day in ["Dienstag", "Mittwoch"] and m_type == "Mittagessen":
                mo_dinner = plan["Montag"]["Abendessen"]
                plan[day][m_type] = {
                    "name": f"Meal Prep: {mo_dinner['name']}",
                    "device": "Mikrowelle",
                    "ingredients": [],
                    "instructions": "Bereits am Montagabend vorgekocht. Einfach aufwärmen!",
                }
            else:
                available = [
                    r
                    for r in st.session_state.recipe_pool[m_type]
                    if filter_recipe(r, exclusions)
                ]
                if available:
                    plan[day][m_type] = random.choice(available)
                else:
                    plan[day][m_type] = {
                        "name": "Kein passendes Rezept gefunden",
                        "device": "-",
                        "ingredients": [],
                        "instructions": "Bitte Ausschlüsse prüfen oder neues Rezept hinzufügen.",
                    }
    return plan


if "current_plan" not in st.session_state:
    st.session_state.current_plan = generate_week()

# --- SIDEBAR NAVIGATION & SETTINGS ---
st.sidebar.title("🌿 NutriCraft Menu")

# Unterseiten Navigation
nav_options = (
    ["📅 " + day for day in DAYS]
    + ["🛒 Einkaufsliste"]
    + ["⭐ Meine Favoriten"]
    + ["➕ Neues Rezept erstellen"]
)
page = st.sidebar.radio("Navigation:", nav_options)

st.sidebar.divider()

# Ausgeschlossene Zutaten verwalten (mit Löschen-Option)
st.sidebar.subheader("🚫 Zutaten-Ausschlüsse")
new_exc = st.sidebar.text_input(
    "Zutat ausschließen:", placeholder="z. B. Pilze, Koriander"
)
if st.sidebar.button("Hinzufügen"):
    if new_exc and new_exc not in st.session_state.exclusions:
        st.session_state.exclusions.append(new_exc)
        st.sidebar.success(f"'{new_exc}' ausgeschlossen!")
        st.rerun()

# Liste der aktuellen Ausschlüsse mit Mülleimer/Löschen-Funktion
if st.session_state.exclusions:
    st.sidebar.write("**Aktuell ausgeschlossen:**")
    for exc in st.session_state.exclusions:
        col_exc_text, col_exc_del = st.sidebar.columns([4, 1])
        col_exc_text.write(f"• {exc}")
        if col_exc_del.button("❌", key=f"del_exc_{exc}"):
            st.session_state.exclusions.remove(exc)
            st.rerun()
else:
    st.sidebar.caption("Keine Zutaten ausgeschlossen.")


# --- MAIN HEADER ---
st.title("🌱 NutriCraft Vegan Studio")

col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.caption(
        "Dein persönlicher Wochenplaner mit Favoriten, Rezepturanleitungen & Meal Prep"
    )
with col_head2:
    if st.button("🎲 Plan neu generieren", use_container_width=True):
        st.session_state.current_plan = generate_week()
        st.rerun()

st.divider()

# --- PAGE: TAGE (Montag bis Sonntag Unterseiten) ---
if page.startswith("📅 "):
    current_day = page.replace("📅 ", "")
    st.header(f"📌 {current_day}")

    for m_type in MEAL_TYPES:
        meal = st.session_state.current_plan[current_day][m_type]

        with st.container():
            st.subheader(f"{m_type}: {meal['name']}")
            st.caption(f"⚙️ Zubereitungsgerät: {meal.get('device', 'Herd')}")

            col_ing, col_inst = st.columns([1, 1.5])

            with col_ing:
                st.write("**🛒 Zutaten (für 2 Personen):**")
                if meal["ingredients"]:
                    for ing in meal["ingredients"]:
                        st.write(
                            f"• {ing['amount']} {ing['unit']} **{ing['item']}**"
                        )
                else:
                    st.info("💡 Meal Prep Gericht.")

            with col_inst:
                st.write("**👩‍🍳 Zubereitung / Rezept:**")
                st.write(meal.get("instructions", "Keine Anleitung vorhanden."))

            # Action Buttons für das Gericht
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                if st.button("❤️ Zu Favoriten", key=f"fav_{current_day}_{m_type}"):
                    if meal not in st.session_state.favorites:
                        st.session_state.favorites.append(meal)
                        st.success("Zu Favoriten hinzugefügt!")
            with btn_col2:
                if not (
                    current_day in ["Dienstag", "Mittwoch"]
                    and m_type == "Mittagessen"
                ):
                    if st.button("🔄 Swap", key=f"swap_{current_day}_{m_type}"):
                        exclusions = st.session_state.exclusions
                        available = [
                            r
                            for r in st.session_state.recipe_pool[m_type]
                            if filter_recipe(r, exclusions)
                            and r["name"] != meal["name"]
                        ]
                        if available:
                            new_meal = random.choice(available)
                            st.session_state.current_plan[current_day][
                                m_type
                            ] = new_meal
                            if (
                                current_day == "Montag"
                                and m_type == "Abendessen"
                            ):
                                prep_title = f"Meal Prep: {new_meal['name']}"
                                st.session_state.current_plan["Dienstag"][
                                    "Mittagessen"
                                ]["name"] = prep_title
                                st.session_state.current_plan["Mittwoch"][
                                    "Mittagessen"
                                ]["name"] = prep_title
                            st.rerun()
            st.divider()

# --- PAGE: EINKAUFSLISTE ---
elif page == "🛒 Einkaufsliste":
    st.header("🛒 Konsolidierte Einkaufsliste für die Woche")

    shopping_list = {}
    for day in DAYS:
        for m_type in MEAL_TYPES:
            meal = st.session_state.current_plan[day][m_type]
            for ing in meal.get("ingredients", []):
                key = (ing["item"], ing["unit"])
                shopping_list[key] = shopping_list.get(key, 0) + ing["amount"]

    if shopping_list:
        df_shopping = pd.DataFrame([
            {"Zutat": k[0], "Menge": v, "Einheit": k[1]}
            for k, v in shopping_list.items()
        ]).sort_values(by="Zutat")

        st.dataframe(df_shopping, use_container_width=True, hide_index=True)

        csv = df_shopping.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Einkaufsliste als CSV herunterladen",
            data=csv,
            file_name="Einkaufsliste_Woche.csv",
            mime="text/csv",
        )
    else:
        st.info("Deine Einkaufsliste ist aktuell leer.")

# --- PAGE: FAVORITEN ---
elif page == "⭐ Meine Favoriten":
    st.header("⭐ Gespeicherte Lieblingsgerichte")

    if st.session_state.favorites:
        for idx, fav in enumerate(st.session_state.favorites):
            with st.expander(f"❤️ {fav['name']} ({fav.get('device', 'Herd')})"):
                st.write("**Zutaten:**")
                for ing in fav.get("ingredients", []):
                    st.write(
                        f"• {ing['amount']} {ing['unit']} **{ing['item']}**"
                    )
                st.write("**Rezept / Anleitung:**")
                st.write(fav.get("instructions", ""))
                if st.button("Aus Favoriten entfernen", key=f"del_fav_{idx}"):
                    st.session_state.favorites.pop(idx)
                    st.rerun()
    else:
        st.info(
            "Du hast noch keine Favoriten gespeichert. Klicke einfach bei einem Gericht auf '❤️ Zu Favoriten'!"
        )

# --- PAGE: NEUES REZEPT ERSTELLEN ---
elif page == "➕ Neues Rezept erstellen":
    st.header("➕ Eigenes Rezept zur Datenbank hinzufügen")

    with st.form("add_recipe_form"):
        rec_name = st.text_input("Rezept Name:")
        rec_cat = st.selectbox("Kategorie:", MEAL_TYPES)
        rec_device = st.text_input(
            "Zubereitungsgerät:", placeholder="z. B. Airfryer, Entsafter, Herd"
        )
        rec_instructions = st.text_area(
            "Zubereitungsanleitung / Rezept Schritt-für-Schritt:"
        )

        st.write("**Zutaten hinzufügen (für 2 Personen):**")
        ing_text = st.text_area(
            "Zutaten zeilenweise eingeben im Format: Menge, Einheit, Zutat\nBeispiel:\n400, g, Tofu\n2, EL, Sojasauce"
        )

        submitted = st.form_submit_button("Rezept speichern")

        if submitted:
            if rec_name and rec_instructions:
                parsed_ingredients = []
                if ing_text:
                    for line in ing_text.split("\n"):
                        parts = [p.strip() for p in line.split(",") if p.strip()]
                        if len(parts) == 3:
                            try:
                                parsed_ingredients.append({
                                    "amount": float(parts[0]),
                                    "unit": parts[1],
                                    "item": parts[2],
                                })
                            except ValueError:
                                pass

                new_recipe = {
                    "name": rec_name,
                    "device": rec_device if rec_device else "Herd",
                    "ingredients": parsed_ingredients,
                    "instructions": rec_instructions,
                }

                st.session_state.recipe_pool[rec_cat].append(new_recipe)
                st.success(
                    f"Rezept '{rec_name}' wurde erfolgreich zu {rec_cat} hinzugefügt!"
                )
            else:
                st.error("Bitte gib mindestens einen Namen und ein Rezept an.")