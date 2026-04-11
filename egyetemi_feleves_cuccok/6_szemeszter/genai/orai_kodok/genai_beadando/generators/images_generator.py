import os
import time
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image


def load_model(model_id: str = "runwayml/stable-diffusion-v1-5",
               use_gpu: bool = True) -> StableDiffusionPipeline | None:
    """
    Betölt egy Stable Diffusion modellt a megadott model ID alapján.

    Args:
        model_id (str, optional): A betöltendő modell azonosítója a Hugging Face Hub-ról. Alapértelmezett: "runwayml/stable-diffusion-v1-5".
        use_gpu (bool, optional): Ha True, és van CUDA elérhető, a modellt GPU-ra tölti. Alapértelmezett: True.

    Returns:
        StableDiffusionPipeline | None: A betöltött pipeline objektum, vagy None, ha a betöltés sikertelen.
    """
    try:
        device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        pipe = pipe.to(device)
        print(f"Modell betöltve: {model_id} ({device})")
        return pipe
    except Exception as e:
        print("Hiba a modell betöltésekor:", str(e))
        return None


def generate_image(pipe: StableDiffusionPipeline, prompt: str, width: int = 512,
                   height: int = 512) -> Image.Image | None:
    """
    Generál egy képet a Stable Diffusion modellel egy adott prompt alapján.

    Args:
        pipe (StableDiffusionPipeline): A betöltött Stable Diffusion pipeline.
        prompt (str): A kép generálásához használt szöveges leírás.
        width (int, optional): A generált kép szélessége pixelben. Alapértelmezett: 512.
        height (int, optional): A generált kép magassága pixelben. Alapértelmezett: 512.

    Returns:
        PIL.Image.Image | None: A generált kép, vagy None, ha hiba történt.
    """
    if pipe is None:
        print("Modell nincs betöltve.")
        return None
    try:
        image = pipe(prompt, height=height, width=width).images[0]
        return image
    except Exception as e:
        print("Hiba a kép generálásakor:", str(e))
        return None


def save_image(image: Image.Image, folder: str = "content/pictures") -> str | None:
    """
    Ment egy PIL képet PNG fájlba az adott mappába.

    Args:
        image (PIL.Image.Image): A menteni kívánt kép.
        folder (str, optional): A célmappa elérési útja. Alapértelmezett: "content/pictures".

    Returns:
        str | None: A mentett fájl elérési útja, vagy None, ha a mentés sikertelen.
    """
    if image is None:
        print("Nincs kép, amit elmenthetnénk.")
        return None
    try:
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"image_{int(time.time())}.png")
        image.save(filename)
        print("Kép mentve ide:", filename)
        return filename
    except Exception as e:
        print("Hiba a kép mentésekor:", str(e))
        return None


def main():
    """
    Főfüggvény, amely a felhasználótól kér promptot, betölti a modellt,
    generálja a képet és elmenti azt.
    """
    prompt = input("Adj meg egy promptot: ")
    pipe = load_model(use_gpu=True)
    image = generate_image(pipe, prompt)
    save_image(image)


if __name__ == "__main__":
    main()
