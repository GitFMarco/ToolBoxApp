from .base_frame import BaseFrame
import tkinter as tk


class HomeFrame(BaseFrame):

    KEY = "home"

    def __init__(self, parent):
        super().__init__(parent)

        # TITLE
        title = self.create_label(self, text="> Cassetta degli attrezzi dello sviluppatore")
        title.pack(expand=True, pady=(100, 0))
        # IMAGE
        image = tk.PhotoImage(file="assets/pixel-pc.png")
        label_image = self.create_label(self, image=image)
        label_image.image = image
        label_image.pack(expand=True, pady=(0, 100))
