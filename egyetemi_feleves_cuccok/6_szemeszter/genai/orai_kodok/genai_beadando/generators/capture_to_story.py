import os
from dotenv import load_dotenv
from fpdf import FPDF
from langchain_groq import ChatGroq

# Betöltjük a .env fájlban található környezeti változókat
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

# GROQ API kulcs beolvasása a környezeti változóból
GROQ_API_KEY = os.getenv("GROQ")


def caption_to_story_groq(caption: str, word_count: int = 500, model_name="llama-3.1-8b-instant") -> str:
    """
    Átalakít egy rövid jelenetleírást (caption) egy részletes, narratív történetté a GROQ API segítségével.

    Args:
        caption (str): A rövid jelenetleírás, amelyből a történet készül.
        word_count (int, optional): A generált történet hozzávetőleges szavainak száma. Alapértelmezett 500.
        model_name (str, optional): A használni kívánt nyelvi modell neve. Alapértelmezett "llama-3.1-8b-instant".

    Returns:
        str: A generált történet szövege. Ha hiba történik, üres stringet ad vissza.

    Raises:
        ValueError: Ha a GROQ API kulcs nincs definiálva a .env fájlban.
    """
    try:
        if not GROQ_API_KEY:
            raise ValueError("A GROQ kulcs nem található a .env fájlban!")

        prompt = (
            f"You are a master storyteller. Tell the following scene as an engaging, imaginative story, "
            f"in the style of a traditional narrator, so it feels like a tale being told aloud to listeners.\n\n"
            f"Scene description:\n{caption}\n\n"
            f"Write approximately {word_count} words, rich in detail and character, immersive and vivid."
        )

        llm = ChatGroq(model=model_name, api_key=GROQ_API_KEY)
        response = llm.invoke(prompt)
        return response.content.strip()

    except Exception as e:
        print(f"Hiba a történet generálásakor: {str(e)}")
        return ""


def save_story_as_pdf(story: str, filepath: str = "content/stories/tale.pdf"):
    """
    Ment egy adott történetet PDF fájlba a megadott elérési útra.

    Args:
        story (str): A menteni kívánt történet szövege.
        filepath (str, optional): A PDF fájl elérési útja. Alapértelmezett "content/stories/tale.pdf".

    Returns:
        None
    """
    if not story:
        print("Nincs menthető történet.")
        return

    try:
        # Létrehozzuk a mappát, ha nem létezik
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # PDF objektum létrehozása és beállítások
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Történet sorainak hozzáadása a PDF-hez
        for line in story.split("\n"):
            pdf.multi_cell(0, 8, line)
            pdf.ln(2)

        pdf.output(filepath)
        print(f"Történet elmentve ide: {filepath}")

    except Exception as e:
        print(f"Hiba a PDF mentésekor: {str(e)}")


if __name__ == "__main__":
    sample_caption = "A small ginger cat is sitting on a wooden fence, looking curiously at a butterfly."

    # Jelenet átalakítása történetté
    story = caption_to_story_groq(sample_caption, word_count=500)

    # Történet mentése PDF-be
    save_story_as_pdf(story, filepath="content/stories/tale.pdf")
