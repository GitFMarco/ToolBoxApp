import os
import tkinter as tk
from .base_frame import BaseFrame


PIXEL_PC_IMAGE_PATH: str = os.path.join(os.path.dirname(__file__), "../assets/pixel-pc.png")


class HomeFrame(BaseFrame):

    KEY = "home"

    def __init__(self, parent):
        super().__init__(parent)

        # TITLE
        title = self.create_label(self, text="> Cassetta degli attrezzi dello sviluppatore")
        title.pack(expand=True, pady=(100, 0))
        # IMAGE
        image = tk.PhotoImage(file=PIXEL_PC_IMAGE_PATH)
        label_image = self.create_label(self, image=image)
        label_image.image = image
        label_image.pack(expand=True, pady=(0, 100))
