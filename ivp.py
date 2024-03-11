import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing GUI")

        # Create a file input button
        self.input_button = tk.Button(root, text="Select Image", command=self.load_image)
        self.input_button.pack()

        # Create a dropdown for selecting filters
        self.filters = ["None", "Grayscale", "Blur", "Canny Edge"]
        self.selected_filter = tk.StringVar(root)
        self.selected_filter.set(self.filters[0])
        self.filter_dropdown = tk.OptionMenu(root, self.selected_filter, *self.filters)
        self.filter_dropdown.pack()

        # Create a process button
        self.process_button = tk.Button(root, text="Process Image", command=self.process_image)
        self.process_button.pack()

        # Create an image display area
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image()

    def process_image(self):
        if self.image is not None:
            filter_choice = self.selected_filter.get()
            if filter_choice == "Grayscale":
                processed_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            elif filter_choice == "Blur":
                processed_image = cv2.GaussianBlur(self.image, (7, 7), 0)
            elif filter_choice == "Canny Edge":
                processed_image = cv2.Canny(self.image, 100, 200)
            else:
                processed_image = self.image

            self.display_image(processed_image)

    def display_image(self, img=None):
        if img is None:
            img = self.image
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=img)
            self.image_label.configure(image=img)
            self.image_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

