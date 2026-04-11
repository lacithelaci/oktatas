import streamlit as st
from pathlib import Path
from generators.text_to_speech import generate_story_audio

# ---------------------------------------------------------
# Streamlit oldal beállítás
# ---------------------------------------------------------
st.set_page_config(
    page_title="PDF to Audio",  # Böngésző címsor
    layout="centered"  # Oldal középre rendezése
)
st.title("PDF to Audio Generator")  # Oldal főcím

# Rövid leírás a felhasználónak
st.markdown(
    """
    Üdv a PDF to Audio oldalon!  
    Itt feltölthetsz egy PDF fájlt, ami tartalmazza a történetedet.  
    A rendszer elkészít belőle egy hangfájlt, amit később akár le is tölthetsz.  
    Csak töltsd fel a PDF-et, majd kattints a **Generate Audio** gombra.
    """
)

# ---------------------------------------------------------
# PDF feltöltése
# ---------------------------------------------------------
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])  # Csak PDF fájlok

if uploaded_file is not None:
    # ---------------------------------------------------------
    # Mentési mappák biztosítása
    # ---------------------------------------------------------
    pdf_folder = Path("../content/stories")  # Célmappa a PDF-eknek
    pdf_folder.mkdir(parents=True, exist_ok=True)  # Mappa létrehozása, ha nem létezik
    pdf_path = pdf_folder / uploaded_file.name  # Teljes útvonal a PDF-nek

    # ---------------------------------------------------------
    # PDF mentése a megadott mappába
    # ---------------------------------------------------------
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())  # Feltöltött fájl tartalmának írása
    st.success(f"PDF uploaded: {uploaded_file.name}")

    # ---------------------------------------------------------
    # Hang generálása gomb
    # ---------------------------------------------------------
    if st.button("Generate Audio"):
        with st.spinner("Generating audio..."):  # Betöltés jelző
            # generate_story_audio() meghívása
            success, result = generate_story_audio(
                pdf_path=str(pdf_path),
                output_folder="content/voice",  # Hangfájlok mappája
                output_filename=pdf_path.stem + ".mp3",  # Hangfájl neve PDF név alapján
                language='en'  # Nyelv beállítása
            )

            if success:
                st.success("Audio generated successfully!")
                st.audio(result, format="audio/mp3")  # Audio lejátszó a Streamlit-ben

                # ---------------------------------------------------------
                # Letöltés gomb
                # ---------------------------------------------------------
                with open(result, "rb") as f:
                    audio_bytes = f.read()  # Hangfájl betöltése memóriába
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name=pdf_path.stem + ".mp3",  # Fájlnév a letöltéshez
                    mime="audio/mpeg"
                )
            else:
                # Hiba esetén üzenet
                st.error(f"Error: {result}")
