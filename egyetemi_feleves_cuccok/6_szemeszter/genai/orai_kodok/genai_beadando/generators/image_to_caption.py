from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# BLIP modell és processzor betöltése
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def generate_caption(image_input) -> str:
    """
    Generál egy rövid leírást (caption) egy adott képről a BLIP modell segítségével.

    Args:
        image_input (str | PIL.Image.Image): A bemeneti kép. Lehet a kép elérési útja (str)
            vagy egy PIL Image objektum.

    Returns:
        str: A generált képleírás (caption). Ha hiba történik, üres stringet ad vissza.

    Example:
        >>> caption = generate_caption("path/to/image.jpg")
        >>> print(caption)
        "A small ginger cat is sitting on a wooden fence, looking curiously at a butterfly."
    """
    try:
        # Kép betöltése, ha útvonal van megadva
        if isinstance(image_input, str):
            image = Image.open(image_input).convert("RGB")
        else:
            image = image_input.convert("RGB")

        # Kép feldolgozása a BLIP modellhez
        inputs = processor(image, return_tensors="pt")

        # Caption generálása
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        print(f"Hiba a caption generálásakor: {str(e)}")
        return ""


if __name__ == "__main__":
    image_path = "content/pictures/image_1774774364.png"

    # Kép leírásának generálása
    caption = generate_caption(image_path)
    print("Caption:", caption)
