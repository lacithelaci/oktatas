import os
from PyPDF2 import PdfReader
from gtts import gTTS


def generate_story_audio(
        pdf_path: str = "content/stories/tale.pdf",
        output_folder: str = "content/voice",
        output_filename: str = "tale.mp3",
        language: str = 'en'
) -> tuple[bool, str]:
    """
    Generál egy hangfájlt egy PDF történetből a Google Text-to-Speech (gTTS) segítségével.

    Args:
        pdf_path (str, optional): A bemeneti PDF fájl elérési útja. Alapértelmezett: "content/stories/tale.pdf".
        output_folder (str, optional): A célmappa a generált hangfájlhoz. Alapértelmezett: "content/voice".
        output_filename (str, optional): A generált MP3 fájl neve. Alapértelmezett: "tale.mp3".
        language (str, optional): A hang nyelve (pl. 'en' az angolhoz, 'hu' a magyarhoz). Alapértelmezett: 'en'.

    Returns:
        tuple[bool, str]: Két értékből álló tuple:
            - bool: True, ha a hang sikeresen generálódott, False, ha hiba történt.
            - str: A generált fájl elérési útja siker esetén, vagy hibaüzenet sikertelenség esetén.

    Raises:
        Exception: Bármilyen hiba, amely a PDF olvasása vagy a TTS generálása során történik,
                   visszatérési értékként jelenik meg a tuple második elemében.

    Example:
        >>> success, path_or_error = generate_story_audio("story.pdf", language='hu')
        >>> if success:
        >>>     print(f"Hangfájl mentve ide: {path_or_error}")
        >>> else:
        >>>     print(f"Hiba történt: {path_or_error}")
    """
    output_path = os.path.join(output_folder, output_filename)

    # Létrehozzuk a kimeneti mappát, ha nem létezik
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        reader = PdfReader(pdf_path)
        full_text = ""

        # PDF oldalak szövegének összegyűjtése
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "

        if not full_text.strip():
            return False, "Empty PDF"

        # Szöveg hangfájlba konvertálása
        tts = gTTS(text=full_text, lang=language)
        tts.save(output_path)

        return True, output_path

    except Exception as e:
        return False, str(e)
