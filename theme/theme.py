import os
import json


THEME_FILE = "theme/theme.json"
DARK = "dark"
LIGHT = "light"


class ToolboxTheme:

    def __init__(self, dark: bool = False):
        theme_mode = self.theme_mode(dark)
        self._theme_config = self.load_theme()
        self.dark = dark
        self._assign_theme_properties(theme_mode)
        self.font_style = self._theme_config['font']

    @classmethod
    def load_theme(cls) -> dict:
        assert os.path.exists(THEME_FILE), "theme.json file missing"
        with open(THEME_FILE, "r") as f:
            return json.load(f)

    @classmethod
    def theme_mode(cls, dark: bool = False) -> str:
        return DARK if dark else LIGHT

    def font(self, font_size: int, bold: bool = False) -> tuple[str, int, str]:
        return self.font_style, font_size, "bold" if bold else ""

    def _assign_theme_properties(self, theme_mode: str):
        assert theme_mode in (DARK, LIGHT)
        self.primary = self._theme_config['mode'][theme_mode]['primary']
        self.secondary = self._theme_config['mode'][theme_mode]['secondary']
        self.accent = self._theme_config['mode'][theme_mode]['accent']
        self.text = self._theme_config['mode'][theme_mode]['text']
        self.background = self._theme_config['mode'][theme_mode]['background']

    def toggle_theme_mode(self):
        self.dark = not self.dark
        theme_mode = self.theme_mode(self.dark)
        self._assign_theme_properties(theme_mode)
