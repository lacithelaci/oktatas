# 11. labor
# =====================================================
# Streamlit alapú generatív MI alkalmazás
# Témák:
# - API-paraméterezés
# - Promptolás (stílus)
# - Kimeneti forma kontroll
# - Kontextus
# - Hibakezelés
#
# Futtatás:
# streamlit run lab10.py
# =====================================================

import streamlit as st
from dotenv import load_dotenv
import json

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------------------------------
# Környezet betöltése
# -----------------------------------------------------
load_dotenv()

st.set_page_config(page_title="Generatív MI – Labor 10", layout="centered")
st.title("Generatív MI – API-alapú szöveggenerálás")

# -----------------------------------------------------
# SIDEBAR – PARAMÉTEREZÉS
# -----------------------------------------------------
st.sidebar.header("Modell beállítások")

temperature = st.sidebar.slider(
    "Temperature (kreativitás)",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Maximális tokenek száma",
    min_value=50,
    max_value=800,
    value=300,
    step=50
)

# -----------------------------------------------------
# FELHASZNÁLÓI BEMENETEK
# -----------------------------------------------------
st.subheader("Feladat")

topic = st.text_input(
    "Miről szeretnél szöveget generálni?",
    placeholder="pl. dinoszauruszok, mesterséges intelligencia, űrutazás"
)

style = st.selectbox(
    "Stílus kiválasztása",
    [
        "Ismeretterjesztő",
        "Gyerekeknek szóló",
        "Humoros",
        "Akadémikus"
    ]
)

output_format = st.selectbox(
    "Kimeneti forma",
    [
        "Folyó szöveg",
        "Bullet pointok",
        "JSON"
    ]
)

# -----------------------------------------------------
# KONTEXTUS
# -----------------------------------------------------
CONTEXT = """
A szöveg egy egyetemi szintű informatikai kurzushoz készül.
A cél az érthetőség, pontosság és a túlzott spekuláció kerülése.
"""

# -----------------------------------------------------
# PROMPT ÖSSZEÁLLÍTÁSA
# -----------------------------------------------------
def build_prompt(topic, style, output_format):
    format_instruction = {
        "Folyó szöveg": "Egy összefüggő, jól tagolt szöveget adj.",
        "Bullet pointok": "Bullet pointokba szedve válaszolj.",
        "JSON": "JSON formátumban válaszolj, 'title' és 'content' mezőkkel."
    }[output_format]

    return f"""
{CONTEXT}

Téma: {topic}
Stílus: {style}

Feladat:
Írj egy szöveget a megadott témáról a kiválasztott stílusban.

Kimeneti forma:
{format_instruction}
"""

# -----------------------------------------------------
# GOMB – GENERÁLÁS
# -----------------------------------------------------
if st.button("✨ Szöveg generálása"):

    if not topic:
        st.warning("Add meg a témát!")
        st.stop()

    try:
        # Modell inicializálása (paraméterezett!)
        model = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=temperature,
            max_tokens=max_tokens
        )

        prompt = ChatPromptTemplate.from_messages([
            ("human", "{input}")
        ])

        chain = prompt | model

        response = chain.invoke({
            "input": build_prompt(topic, style, output_format)
        })

        st.success("Kész!")

        # -------------------------------------------------
        # KIMENET MEGJELENÍTÉSE (FORMÁTUMFÜGGŐ)
        # -------------------------------------------------
        if output_format == "JSON":
            try:
                parsed = json.loads(response.content)
                st.json(parsed)
            except json.JSONDecodeError:
                st.error("A modell nem érvényes JSON-t adott vissza.")
                st.text(response.content)
        else:
            st.write(response.content)

    except Exception as e:
        # -------------------------------------------------
        # HIBAKEZELÉS
        # -------------------------------------------------
        st.error("Hiba történt a generálás során.")
        st.exception(e)
