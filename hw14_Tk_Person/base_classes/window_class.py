from tkinter import *


class Window(Tk):
    FORM_WIDTH = 900
    FORM_HEIGHT = 600
    bg_all = "#ADD8E6"

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.winfo_screenwidth()
        self.winfo_screenheight()
        self.title('Person')
        self['bg'] = self.bg_all

        self.resizable(width=False, height=False)
        self.geometry(f"{self.FORM_WIDTH}x{self.FORM_HEIGHT}+"
                             f"{self.winfo_screenwidth() // 2 - self.FORM_WIDTH // 2}"
                             f"+{self.winfo_screenheight() // 2 - self.FORM_HEIGHT // 2}")

