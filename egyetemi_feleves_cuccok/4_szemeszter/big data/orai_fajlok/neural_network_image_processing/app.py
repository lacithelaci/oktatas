import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw
import tensorflow as tf
from tensorflow import keras


class MNISTDrawingApp:
    def __init__(self, root, model_path="mnist_simple.keras"):
        self.root = root
        self.root.title("MNIST Számfelismerés - Rajzolj és Találd ki!")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        try:
            self.model = keras.models.load_model(model_path)
            print(f"Modell sikeresen betöltve: {model_path}")
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült betölteni a modellt:\n{e}")
            self.root.destroy()
            return

        self.canvas_width = 280
        self.canvas_height = 280
        self.brush_size = 15
        self.drawing = False

        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text="Rajzolj egy számjegyet (0-9)",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        title_label.pack(pady=10)

        canvas_frame = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=2)
        canvas_frame.pack(pady=10, padx=10)

        self.canvas = tk.Canvas(
            canvas_frame,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white",
            cursor="cross",
            relief=tk.SUNKEN,
            bd=2
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.result_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(
            self.result_frame,
            text="Rajzolj valamit, majd kattints az 'Előrejelzés' gombra!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        self.result_label.pack()

        self.confidence_label = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#999"
        )
        self.confidence_label.pack()

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=15)

        self.predict_btn = tk.Button(
            button_frame,
            text="Előrejelzés",
            command=self.predict,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.predict_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(
            button_frame,
            text="Törlés",
            command=self.clear_canvas,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.clear_btn.grid(row=0, column=1, padx=5)

        info_frame = tk.Frame(self.root, bg="#e3f2fd", relief=tk.FLAT, bd=1)
        info_frame.pack(pady=10, padx=10, fill=tk.X)

        info_text = tk.Label(
            info_frame,
            text="Tipp: Középen rajzolj, ne túl kicsi legyen! A modell 28x28-as felbontást használ.",
            font=("Arial", 9),
            bg="#e3f2fd",
            fg="#1976d2",
            wraplength=500,
            justify=tk.LEFT
        )
        info_text.pack(padx=10, pady=8)

    def start_draw(self, event):
        self.drawing = True
        self.draw_point(event.x, event.y)

    def draw_line(self, event):
        if self.drawing:
            self.draw_point(event.x, event.y)

    def stop_draw(self, event):
        self.drawing = False

    def draw_point(self, x, y):
        """Kört rajzol az egér pozíciójánál"""
        r = self.brush_size // 2
        if 0 <= x < self.canvas_width and 0 <= y < self.canvas_height:
            # Rajzolás PIL image-re (0 = fekete)
            self.draw.ellipse([x - r, y - r, x + r, y + r], fill=0)
            # Rajzolás GUI-ra
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")

    def predict(self):
        """Előrejelzés futtatása"""
        try:
            img_resized = self.image.resize((28, 28))

            img_array = np.array(img_resized, dtype=np.float32) / 255.0

            img_array = 1.0 - img_array

            img_input = img_array.reshape(1, 28, 28)

            predictions = self.model.predict(img_input, verbose=0)
            predicted_digit = np.argmax(predictions[0])
            confidence = predictions[0][predicted_digit] * 100

            self.result_label.config(
                text=f"Felismert szám: {predicted_digit}",
                fg="#2e7d32",
                font=("Arial", 14, "bold")
            )

            top_3_indices = np.argsort(predictions[0])[-3:][::-1]
            conf_text = f"Biztonság: {confidence:.1f}%"
            self.confidence_label.config(text=conf_text)

        except Exception as e:
            messagebox.showerror("Hiba", f"Előrejelzés sikertelen:\n{e}")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=255)
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="Rajzolj valamit, majd kattints az 'Előrejelzés' gombra!", fg="#666")
        self.confidence_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = MNISTDrawingApp(root, model_path="mnist_simple.keras")
    root.mainloop()