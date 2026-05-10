# Futtatás: streamlit run lab12.py
# =====================================================
# Streamlit Best Practices
# =====================================================
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import json
from datetime import datetime
from pathlib import Path

load_dotenv()

STORIES_FILE = "stories.json"

def load_stories():
    if Path(STORIES_FILE).exists():
        with open(STORIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_stories(stories):
    with open(STORIES_FILE, "w", encoding="utf-8") as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)

st.set_page_config(page_title="Advanced Streamlit", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []
if "generated_stories" not in st.session_state:
    st.session_state.generated_stories = load_stories()

st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #1E88E5;}
    .success-box {background-color: #E8F5E9; padding: 1rem; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("Advanced Streamlit")
st.markdown("### Hogyan készítsünk professzionális Generatív MI alkalmazást?")

with st.sidebar:
    st.header("Beállítások")
    model = st.selectbox(
        "Modell választása",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max Tokens", 100, 1000, 500, 50)

tab1, tab2 = st.tabs(["⚙️ Mese Generálás", "📜 Előzmények"])

with tab1:
    st.subheader("Személyre szabott mese generálása")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Gyerek neve", value="Lilla")
        age = st.number_input("Kor", min_value=4, max_value=12, value=7)
        
    with col2:
        interest = st.text_input("Érdeklődési kör", value="sárkányok és varázslat")
        style = st.selectbox("Stílus", ["Vidám", "Kalandos", "Tanulságos", "Humoros"])

    if st.button("Generálj mesét", type="primary"):
        with st.spinner("Groq dolgozik..."):
            try:
                llm = ChatGroq(model=model, temperature=temperature, max_tokens=max_tokens)
                prompt = f"""
                Írj egy rövid, {style.lower()} mesét {name} nevű {age} éves gyereknek, 
                aki nagyon szereti a(z) {interest}.
                """
                response = llm.invoke(prompt)
                story = response.content

                st.session_state.generated_stories.append({
                    "name": name,
                    "age": age,
                    "interest": interest,
                    "style": style,
                    "story": story,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })

                save_stories(st.session_state.generated_stories)  # ← fájlba ment

                st.success("Mese elkészült!")
                st.write(story)
            except Exception as e:
                st.error(f"Hiba történt: {str(e)}")

with tab2:
    st.subheader("Korábbi generálások")
    
    if st.session_state.generated_stories:
        for i, entry in enumerate(reversed(st.session_state.generated_stories)):
            with st.expander(f"{entry['timestamp']} – {entry['name']} ({entry['interest']})"):
                st.write(entry['story'])
    else:
        st.info("Még nincs generált mese.")

if st.session_state.generated_stories:
    last_story = st.session_state.generated_stories[-1]
    
    story_text = f"Mese {last_story['name']} számára\n\n{last_story['story']}"
    
    st.download_button(
        label="📥 Letöltés TXT formátumban",
        data=story_text,
        file_name=f"mese_{last_story['name']}.txt",
        mime="text/plain"
    )

st.caption("Generatív MI kurzus – Advanced Streamlit")