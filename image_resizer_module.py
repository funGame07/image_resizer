from tkinter import *
from PIL import Image, ImageTk

class Resize():
    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height
    
    def resizing_image(self):
        image = Image.open(self.path).resize((self.width, self.height), resample=Image.LANCZOS)
        image.save(self.path)
        return ImageTk.PhotoImage(image)



