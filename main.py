from theme.theme import ToolboxTheme
from app.app import ToolboxApp


if __name__ == "__main__":
    active_theme = ToolboxTheme(dark=True)
    app = ToolboxApp(active_theme)
    app.mainloop()
