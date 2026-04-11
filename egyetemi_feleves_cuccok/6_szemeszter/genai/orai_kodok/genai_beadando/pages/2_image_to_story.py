import streamlit as st
from PIL import Image

# Saját modulok importálása
from generators.image_to_caption import generate_caption
from generators.capture_to_story import caption_to_story_groq, save_story_as_pdf

# ---------------------------------------------------------
# Streamlit oldal beállítás
# ---------------------------------------------------------
st.set_page_config(
    page_title="Image to Story",  # Böngésző címsor
    layout="centered"  # Oldal középre rendezése
)
st.title("Image to Story Generator")  # Oldal főcím

# Rövid leírás a felhasználónak
st.markdown(
    """
    Üdv a Mesélő Képalkotóban!  
    Itt feltölthetsz egy képet, és a mesterséges intelligencia készít róla egy rövid **caption-t**, majd ebből egy **mese-szerű történetet**.  
    Csak tölts fel egy képet, állítsd be a kívánt történet hosszát, majd kattints a **Generate story** gombra!  
    Ha kész a történet, akár **PDF formátumban is elmentheted**.
    """
)

# ---------------------------------------------------------
# Kép feltöltése
# ---------------------------------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])  # Csak képfájlok

# ---------------------------------------------------------
# Session state inicializálás
# ---------------------------------------------------------
# Ezzel megőrizzük a caption és story értékét az oldalon frissítések között
if "caption" not in st.session_state:
    st.session_state.caption = None
if "story" not in st.session_state:
    st.session_state.story = None

# ---------------------------------------------------------
# Ha van feltöltött kép
# ---------------------------------------------------------
if uploaded_file is not None:
    # Kép megnyitása
    image = Image.open(uploaded_file)
    # Kép megjelenítése az alkalmazásban
    st.image(image, caption="Uploaded image", width='stretch')

    # ---------------------------------------------------------
    # Story hossz beállítása sliderrel
    # ---------------------------------------------------------
    word_count = st.slider("Story length (words)", 100, 1000, 500)  # Minimum 100, maximum 1000 szó, alapértelmezett 500

    # ---------------------------------------------------------
    # Story generálás gomb esemény
    # ---------------------------------------------------------
    if st.button("Generate story"):
        # ---------------------------------------------------------
        # Caption generálása a feltöltött képből
        # ---------------------------------------------------------
        with st.spinner("Generating caption..."):  # Betöltés jelző
            caption = generate_caption(image)
            st.session_state.caption = caption  # Session state-be mentés

        # ---------------------------------------------------------
        # Story generálása a caption alapján
        # ---------------------------------------------------------
        with st.spinner("Generating story..."):  # Betöltés jelző
            story = caption_to_story_groq(caption, word_count=word_count)
            st.session_state.story = story  # Session state-be mentés

# ---------------------------------------------------------
# Caption megjelenítése
# ---------------------------------------------------------
if st.session_state.caption:
    st.subheader("Generated caption")
    st.write(st.session_state.caption)

# ---------------------------------------------------------
# Story megjelenítése
# ---------------------------------------------------------
if st.session_state.story:
    st.subheader("Generated story")
    st.write(st.session_state.story)

    # ---------------------------------------------------------
    # PDF mentés gomb
    # ---------------------------------------------------------
    if st.button("Save as PDF"):
        save_story_as_pdf(st.session_state.story)
        st.success("Story saved as PDF")
