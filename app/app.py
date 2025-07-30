import os
import tkinter as tk
from theme.theme import ToolboxTheme
from frames.module_creator import ModuleCreatorFrame
from frames.home import HomeFrame


APP_ICON_PATH: str = os.path.join(os.path.dirname(__file__), "../assets/icon.ico")

SECTIONS = {
    'Odoo': {
        ModuleCreatorFrame.KEY: "> Crea Modulo"
    },
    'In arrivo nuove funzioni...': {

    }
}


class ToolboxApp(tk.Tk):

    def __init__(self, theme: ToolboxTheme):
        super().__init__()

        # -- APP APPEARANCE -- #
        self.title("Cassetta degli attrezzi")
        self.geometry("800x500")
        self.config(cursor="plus")
        self.minsize(600, 400)
        self.iconbitmap(APP_ICON_PATH)

        # -- THEME -- #
        self.theme = theme

        # -- RIGHT CONTENT -- #
        self.content = tk.Frame(self, bg=self.theme.background)
        self.content.pack(side="right", fill="both", expand=True)

        # -- LEFT SIDEBAR -- #
        self.sidebar = tk.Frame(self, width=180, bg=self.theme.primary, relief="ridge", border=5)
        self.sidebar.pack(side="left", fill="y")

        # Sidebar menus (variable used only to highlight selected button)
        self.sidebar_menus = {}

        # Home button
        home_btn = self.create_button(parent=self.sidebar, label="> Home", command=lambda: self.show_frame(HomeFrame.KEY))
        home_btn.pack(fill="x", pady=(10, 5))
        self.sidebar_menus[HomeFrame.KEY] = home_btn

        # Sections
        for section_name, buttons in SECTIONS.items():
            # Section label
            label = tk.Label(
                self.sidebar,
                text=section_name,
                bg=self.theme.primary, fg=self.theme.text,
                anchor="w", padx=10,
                font=self.theme.font(10, bold=True)
            )
            label.pack(fill="x", pady=(10, 0))
            # Section menus
            for name, label_text in buttons.items():
                menu = self.create_button(parent=self.sidebar, label=label_text, command=lambda: self.show_frame(name))
                menu.pack(fill="x", pady=1)
                self.sidebar_menus[name] = menu

        # -- FRAME LOADING -- #
        self.frames = {
            HomeFrame.KEY: HomeFrame(self.content),
            ModuleCreatorFrame.KEY: ModuleCreatorFrame(self.content),
        }

        self.current_frame = None
        self.show_frame(HomeFrame.KEY)

    def create_button(self, parent=None, label: str = None, command=None, primary: bool = True, font_color: str = None, background: str = None) -> tk.Button:
        """
        :returns: A themed button
        """
        return tk.Button(
            master=parent,
            text=label,
            command=command,
            anchor="w",
            padx=10,
            font=self.theme.font(10, bold=True),
            cursor="dotbox",
            relief="raised",
            border=5,
            fg=font_color or self.theme.text,
            bg=background or self.theme.primary if primary else self.theme.secondary
        )

    def show_frame(self, name) -> None:
        """Hides current frame and displays the one with the specified name"""
        # Hide current frame
        if self.current_frame:
            self.current_frame.pack_forget()

        # Show new frame
        frame = self.frames[name]
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.highlight_button(name)

    def highlight_button(self, active_name) -> None:
        """Highlights the menù button of the given frame name (active_name). Deactivates (visually) the others."""
        for name, btn in self.sidebar_menus.items():
            if name == active_name:
                btn.config(bg=self.theme.accent, relief="sunken")
            else:
                btn.config(bg=self.theme.secondary, relief="raised")
