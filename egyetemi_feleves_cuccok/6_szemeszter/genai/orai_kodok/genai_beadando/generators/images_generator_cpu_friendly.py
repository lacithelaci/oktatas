import os
import time
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image


def load_model(model_id: str = "runwayml/stable-diffusion-v1-5",
               use_gpu: bool = False) -> StableDiffusionPipeline | None:
    """
    Betölt egy Stable Diffusion modellt a megadott model ID alapján.

    A modellt GPU-ra vagy CPU-ra tölti a `use_gpu` paramétertől és a rendelkezésre álló hardvertől függően.
    GPU esetén float16, CPU esetén float32 precizitás kerül beállításra.

    Args:
        model_id (str, optional): A betöltendő modell azonosítója a Hugging Face Hub-ról. Alapértelmezett: "runwayml/stable-diffusion-v1-5".
        use_gpu (bool, optional): Ha True és van CUDA elérhető, a modellt GPU-ra tölti. Alapértelmezett: False.

    Returns:
        StableDiffusionPipeline | None: A betöltött pipeline objektum, vagy None, ha a betöltés sikertelen.
    """
    device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
    try:
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


def generate_image(pipe: StableDiffusionPipeline, prompt: str, width: int = 32, height: int = 32,
                   steps: int = 10) -> Image.Image | None:
    """
    Generál egy képet a Stable Diffusion modellt használva egy adott prompt alapján.

    Args:
        pipe (StableDiffusionPipeline): A betöltött Stable Diffusion pipeline objektum.
        prompt (str): Szöveges leírás a generálandó képhez.
        width (int, optional): A generált kép szélessége pixelben. Alapértelmezett: 32 (CPU-barát).
        height (int, optional): A generált kép magassága pixelben. Alapértelmezett: 32 (CPU-barát).
        steps (int, optional): A generálás lépésszáma (num_inference_steps). Alapértelmezett: 10.

    Returns:
        PIL.Image.Image | None: A generált kép, vagy None, ha hiba történt.
    """
    if pipe is None:
        print("Modell nincs betöltve.")
        return None
    try:
        image = pipe(prompt, height=height, width=width, num_inference_steps=steps).images[0]
        return image
    except Exception as e:
        print("Hiba a kép generálásakor:", str(e))
        return None


def save_image(image: Image.Image, folder: str = "content/pictures") -> str | None:
    """
    Ment egy PIL képet PNG fájlba a megadott mappába.

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
    Főfüggvény, amely:

    1. Bekéri a felhasználótól a promptot.
    2. Betölti a modellt CPU-ra.
    3. Generál egy képet a megadott paraméterekkel.
    4. Menteni a generált képet PNG formátumban.
    5. Kiírja a teljes futási időt.
    """
    prompt = input("Adj meg egy promptot: ")
    start = time.time()

    pipe = load_model(use_gpu=False)  # CPU-barát mód
    image = generate_image(pipe, prompt, width=128, height=128, steps=50)
    save_image(image)

    print(f"Futási idő: {time.time() - start:.2f} másodperc")


if __name__ == "__main__":
    main()
