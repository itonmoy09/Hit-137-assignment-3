import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Multiple inheritance: Combining functionalities of tk.Tk and our custom mixin classes
class ImageClassificationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Classification App")
        self.geometry("500x500")
        self.model = self.load_model()
        self.setup_ui()

    # Encapsulation: Keeping model loading logic inside a method
    def load_model(self):
        # Loading a pre-trained MobileNetV2 model + weights
        model = tf.keras.applications.MobileNetV2(weights='imagenet')
        return model

    # Encapsulation: Setting up the UI inside a method
    def setup_ui(self):
        self.label = ttk.Label(self, text="Upload an image to classify")
        self.label.pack(pady=20)

        self.upload_button = ttk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=20)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=20)

    # Method overriding: Overriding the built-in destroy method to add a confirmation
    def destroy(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            super().destroy()

    # Polymorphism: Using a decorator to modify behavior of methods
    def catch_errors(method):
        def wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        return wrapper

    @catch_errors
    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((224, 224))  # Resizing image for the model
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

            predictions = self.model.predict(img_array)
            decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
            self.display_image(img)
            self.display_result(decoded_predictions)

    def display_image(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk  # Keeping a reference to avoid garbage collection

    def display_result(self, predictions):
        result_text = f"Prediction: {predictions[0][1]}, Confidence: {predictions[0][2]:.2f}"
        self.result_label.configure(text=result_text)

if __name__ == "__main__":
    app = ImageClassificationApp()
    app.mainloop()
