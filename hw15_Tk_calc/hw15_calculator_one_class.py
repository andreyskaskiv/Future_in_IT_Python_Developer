from tkinter import *


class Calculator(Tk):
    FORM_WIDTH = 350
    FORM_HEIGHT = 425
    BG_ALL = '#07575B'
    BG_BUTTON = "#C4DFE6"
    TITLE = "Calculator"

    def __init__(self):
        super().__init__()
        self.title(self.TITLE)
        self.winfo_screenwidth()
        self.winfo_screenheight()
        self['bg'] = self.BG_ALL
        self.resizable(width=False, height=False)
        self.geometry(f"{self.FORM_WIDTH}x{self.FORM_HEIGHT}+"
                      f"{self.winfo_screenwidth() // 2 - self.FORM_WIDTH // 2}"
                      f"+{self.winfo_screenheight() // 2 - self.FORM_HEIGHT // 2}")

        self.equation = ''
        self.lbl = Label(text=self.equation, font=("Arial Bold", 42), bg=self.BG_ALL, foreground="#FFF")
        self.lbl.place(x=0, y=1)

        self.digits = {
            '(': (0, 80), ')': (90, 80), '🡸': (180, 80), '/': (270, 80),  # (x=, y=)
            '1': (0, 150), '2': (90, 150), '3': (180, 150), '*': (270, 150),
            '4': (0, 220), '5': (90, 220), '6': (180, 220), '-': (270, 220),
            '7': (0, 290), '8': (90, 290), '9': (180, 290), '+': (270, 290),
            'C': (0, 360), '0': (90, 360), '.': (180, 360), '=': (270, 360),
        }

        self.create_symbol_buttons()

    def create_symbol_buttons(self):
        for symbol, grid_value in self.digits.items():
            command = lambda x=symbol: self.solve(x)
            Button(self, width=4, height=1,
                   text=symbol,
                   relief='flat',
                   bg=self.BG_BUTTON,
                   font=("Arial", 22, "bold"),
                   command=command).place(x=grid_value[0], y=grid_value[1])

    def solve(self, operation):
        self.equation = str(
            {"C": lambda s: "",
             "🡸": lambda s: s[:-1],
             "=": lambda s: eval(s)}.get(
                operation, lambda s: (s if s != "0" else "") + operation)(
                self.equation)) or "0"
        self.lbl.configure(text=self.equation)


if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
