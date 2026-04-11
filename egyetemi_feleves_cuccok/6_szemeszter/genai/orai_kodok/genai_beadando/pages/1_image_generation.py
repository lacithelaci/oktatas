import streamlit as st
from PIL import Image
from generators.images_generator import load_model, generate_image, save_image
from io import BytesIO  # Memóriában lévő fájlok kezelésére

# ---------------------------------------------------------
# Streamlit oldal beállítás
# ---------------------------------------------------------
st.set_page_config(
    page_title="Stable Diffusion Image Generator",  # Böngésző címsor
    layout="centered"  # Oldal középre rendezése
)
st.title("Stable Diffusion Image Generator")  # Oldal főcím

# Rövid leírás a felhasználónak
st.markdown(
    """
    Adj meg egy promptot, és a mesterséges intelligencia generál egy képet belőle!  
    Amint elkészült a kép, megtekintheted, és le is töltheted PNG formátumban.
    """
)

# ---------------------------------------------------------
# Prompt bevitele
# ---------------------------------------------------------
prompt = st.text_input("Enter your prompt:")  # Felhasználói szövegmező

# ---------------------------------------------------------
# Kép generálás gomb esemény
# ---------------------------------------------------------
if st.button("Generate Image") and prompt:  # Csak ha prompt is van
    with st.spinner("Loading model and generating image..."):  # Betöltés jelző
        # ---------------------------------------------------------
        # Modell betöltése (GPU használatával)
        # ---------------------------------------------------------
        pipe = load_model(use_gpu=True)

        # ---------------------------------------------------------
        # Kép generálása a prompt alapján
        # ---------------------------------------------------------
        image = generate_image(pipe, prompt)

        if image:
            # ---------------------------------------------------------
            # Kép mentése fájlba
            # ---------------------------------------------------------
            filename = save_image(image)

            # ---------------------------------------------------------
            # Kép megjelenítése az alkalmazásban
            # ---------------------------------------------------------
            st.image(image, caption="Generated Image", width='stretch')

            # ---------------------------------------------------------
            # Letöltés gomb előkészítése
            # ---------------------------------------------------------
            buffer = BytesIO()  # Memóriába mentés
            image.save(buffer, format="PNG")
            buffer.seek(0)  # Mutató vissza a fájl elejére
            st.download_button(
                label="Download Image",
                data=buffer,
                file_name=filename.split("/")[-1],  # Csak a fájlnév
                mime="image/png"
            )
        else:
            # Hiba esetén üzenet
            st.error("Error generating image. Please try again.")