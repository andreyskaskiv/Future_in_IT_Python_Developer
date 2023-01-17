from tkinter import *
from string import ascii_lowercase, ascii_uppercase

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Window(Tk):
    FORM_WIDTH = 900
    FORM_HEIGHT = 150
    bg_all = "#ADD8E6"

    def __init__(self):
        super().__init__()
        self.winfo_screenwidth()
        self.winfo_screenheight()
        self.title('Person')
        self['bg'] = self.bg_all

        self.resizable(width=False, height=False)
        self.geometry(f"{self.FORM_WIDTH}x{self.FORM_HEIGHT}+"
                      f"{self.winfo_screenwidth() // 2 - self.FORM_WIDTH // 2}"
                      f"+{self.winfo_screenheight() // 2 - self.FORM_HEIGHT // 2}")


class UserName:
    bg_all = "#ADD8E6"
    __ALPHABET_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    __ALPHABET_UPPER_UA = __ALPHABET_UA.upper()
    __AGE_MIN = 16
    __AGE_MAX = 66

    def __init__(self, canvas_win):
        self.canvas_win = canvas_win
        self.username = StringVar()
        self.check_username = StringVar()

        self.user_frame = self.create_user_frame()
        self.create_user_label()

    def create_user_label(self):
        sample_username_label = Label(self.user_frame, text="Приклад:",
                                      bg=self.bg_all,
                                      justify=LEFT,
                                      font=("Arial", 16))

        sample_info_username_label = Label(self.user_frame, text="Зеленський Володимир Олександрович",
                                           bg=self.bg_all,
                                           justify=LEFT,
                                           font=("Arial", 16))

        info_username_label = Label(self.user_frame, text="П.І.Б.:",
                                    bg=self.bg_all,
                                    justify=LEFT,
                                    font=("Arial", 16, "bold"))

        username_entry = Entry(self.user_frame, width=30,
                               borderwidth=3,
                               textvariable=self.username,
                               font=("Comic Sans MS", 14))

        valid_username_label = Label(textvariable=self.check_username,
                                     bg=self.bg_all,
                                     justify=LEFT,
                                     font=("Arial", 10, "bold"))

        self.username.trace_add("write", self.check_username_input)

        sample_username_label.place(x=0, y=0)
        sample_info_username_label.place(x=150, y=0)
        #
        info_username_label.place(x=0, y=30)
        username_entry.place(x=150, y=30)
        valid_username_label.place(x=530, y=30)

    def check_username_input(self, *args):
        name = self.username.get().split()
        if len(name) != 3:
            return self.check_username.set("⇑ Неправильний формат запису ПІБ, дивись приклад ⇑")

        letters = ascii_lowercase + ascii_uppercase + self.__ALPHABET_UA + self.__ALPHABET_UPPER_UA + '-'
        for symbol in name:
            if len(symbol) < 1:
                return self.check_username.set("У ПІБ має бути хоча б один символ")
            if len(symbol.strip(letters)) != 0:
                return self.check_username.set("У ПІБ можна використовувати лише буквені символи та дефіс")
        return self.check_username.set("✔")

    def create_user_frame(self):
        frame = Frame(self.canvas_win, bg=self.bg_all)
        frame.pack(expand=True, fill="both")
        return frame


class Age:
    __AGE_MIN = 16
    __AGE_MAX = 66
    bg_all = "#ADD8E6"

    def __init__(self, canvas_win):
        self.canvas_win = canvas_win

        self.age = StringVar()
        self.check_age = StringVar()

        self.age_frame = self.create_age_frame()
        self.create_age_label()

    def create_age_label(self):
        sample_age_label = Label(self.age_frame, text="Вік в діапазоні:",
                                 bg=self.bg_all,
                                 justify=LEFT,
                                 font=("Arial", 16))

        sample_info_age_label = Label(self.age_frame, text=f"от {Age.__AGE_MIN} до {Age.__AGE_MAX}",
                                      bg=self.bg_all,
                                      justify=LEFT,
                                      font=("Arial", 16))

        info_age_label = Label(self.age_frame, text="Вік:",
                               bg=self.bg_all,
                               justify=LEFT,
                               font=("Arial", 16, "bold"))

        age_entry = Entry(self.age_frame, width=30,
                          borderwidth=3,
                          textvariable=self.age,
                          font=("Comic Sans MS", 14))

        valid_age_label = Label(textvariable=self.check_age,
                                bg=self.bg_all,
                                justify=LEFT,
                                font=("Arial", 10, "bold"))

        self.age.trace_add("write", self.check_age_input)

        sample_age_label.place(x=0, y=0)
        sample_info_age_label.place(x=150, y=0)
        #
        info_age_label.place(x=0, y=30)
        age_entry.place(x=150, y=30)
        valid_age_label.place(x=530, y=110)

    def check_age_input(self, *args):
        age = self.age.get()
        for number in age:
            if not number.isdigit():
                return self.check_age.set('only digit')

        age = int(age)
        if age < self.__AGE_MIN or age > self.__AGE_MAX:
            return self.check_age.set("Вік не у діапазоні")
        return self.check_age.set("✔")

    def create_age_frame(self):
        frame = Frame(self.canvas_win, bg=self.bg_all)
        frame.pack(expand=True, fill="both")
        return frame


class MainApp:
    def __init__(self):
        self.canvas = Window()
        self.my_user = UserName(self.canvas)
        self.my_age = Age(self.canvas)

    def run(self):
        self.canvas.mainloop()


if __name__ == '__main__':
    person = MainApp()
    person.run()
