import streamlit as st

st.set_page_config(page_title="Generative AI Hub", layout="wide")
st.title("Welcome to the Generative AI Hub")

st.markdown("""
Üdv a Generatív AI projektben!  

Ez az alkalmazás lehetővé teszi, hogy mesterséges intelligenciát használva:  

- **Image → Story**: Feltöltesz egy képet, és a rendszer készít róla rövid összefoglalót, majd egy teljes történetet.  
- **PDF → Audio**: Feltöltesz egy PDF-et, és a rendszer hangfájlt készít belőle (gTTS).  
- **Prompt → AI Image**: Megadsz egy promptot, és a Stable Diffusion AI generál egy képet belőle.  

Használd a bal oldali menüt az oldalak közötti váltáshoz!
""")