from tkinter import Frame, Label, Button


class BaseFrame(Frame):
    """
    Base of a Toolbox App main frame
    """

    KEY: str = None

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        assert self.KEY, "KEY parameter is required for a Frame in this app"

        # Gather app theme info
        app = parent.winfo_toplevel()
        self.theme = app.theme

        self.config(bg=self.theme.background)
        self.fg = self.theme.text
        self.font = self.theme.font(12)

    def create_subframe(self, master=None, cnf={}, **kwargs) -> Frame:
        """Create and returns a themed child subframe"""
        kwargs.setdefault("bg", self.theme.background)
        return Frame(master=master, cnf=cnf, **kwargs)

    def create_label(self, master=None, cnf={}, **kwargs) -> Label:
        """Create and returns a themed label"""
        font_size: int = kwargs.pop('font_size', 15)
        bold: bool = kwargs.pop('bold', False)
        kwargs.setdefault("bg", self.theme.background)
        kwargs.setdefault("fg", self.theme.text)
        kwargs.setdefault("font", self.theme.font(font_size, bold))
        return Label(master=master, cnf=cnf, **kwargs)

    def create_button(self, master=None, cnf={}, **kwargs) -> Button:
        """Create and returns a themed button"""
        primary: bool = kwargs.pop('primary', False)
        kwargs.setdefault("bg", self.theme.primary if primary else self.theme.secondary)
        kwargs.setdefault("fg", self.theme.text)
        kwargs.setdefault("font", self.theme.font(10, bold=True))
        kwargs.setdefault("cursor", "dotbox")
        kwargs.setdefault("relief", "raised")
        kwargs.setdefault("border", 5)
        return Button(master=master, cnf=cnf, **kwargs)
