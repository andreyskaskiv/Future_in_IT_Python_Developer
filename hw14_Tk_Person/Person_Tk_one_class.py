from tkinter import *
from string import ascii_lowercase, ascii_uppercase


class Window(Tk):
    FORM_WIDTH = 900
    FORM_HEIGHT = 600
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


class User(Window):
    __ALPHABET_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    __ALPHABET_UPPER_UA = __ALPHABET_UA.upper()
    __AGE_MIN = 16
    __AGE_MAX = 66

    def __init__(self):
        super().__init__()

        # User

    def get_user(self):
        self.username = StringVar()
        self.check_username = StringVar()

        self.sample_username_label = Label(self, text="Приклад:",
                                           bg=self.bg_all,
                                           justify=LEFT,
                                           font=("Arial", 16))

        self.sample_info_username_label = Label(self, text="Зеленський Володимир Олександрович",
                                                bg=self.bg_all,
                                                justify=LEFT,
                                                font=("Arial", 16))

        self.info_username_label = Label(self, text="П.І.Б.:",
                                         bg=self.bg_all,
                                         justify=LEFT,
                                         font=("Arial", 16, "bold"))

        self.username_entry = Entry(self, width=30,
                                    borderwidth=3,
                                    textvariable=self.username,
                                    font=("Comic Sans MS", 14))

        self.valid_username_label = Label(textvariable=self.check_username,
                                          bg=self.bg_all,
                                          justify=LEFT,
                                          font=("Arial", 10, "bold"))

        self.username.trace_add("write", self.check_username_input)

        # Age

    def get_age(self):
        self.age = StringVar()
        self.check_age = StringVar()

        self.sample_age_label = Label(self, text="Вік в діапазоні: ",
                                      bg=self.bg_all,
                                      justify=LEFT,
                                      font=("Arial", 16))

        self.sample_info_age_label = Label(self, text=f"от {self.__AGE_MIN} до {self.__AGE_MAX}",
                                           bg=self.bg_all,
                                           justify=LEFT,
                                           font=("Arial", 16))

        self.info_age_label = Label(self, text="Вік:",
                                    bg=self.bg_all,
                                    justify=LEFT,
                                    font=("Arial", 16, "bold"))

        self.age_entry = Entry(self, width=30,
                               borderwidth=3,
                               textvariable=self.age,
                               font=("Comic Sans MS", 14))

        self.valid_age_label = Label(textvariable=self.check_age,
                                     bg=self.bg_all,
                                     justify=LEFT,
                                     font=("Arial", 10, "bold"))

        self.age.trace_add("write", self.check_age_input)

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

    def check_age_input(self, *args):
        age = self.age.get()
        for number in age:
            if not number.isdigit():
                return self.check_age.set('only digit')

        age = int(age)
        if age < self.__AGE_MIN or age > self.__AGE_MAX:
            return self.check_age.set("Вік не у діапазоні")
        return self.check_age.set("✔")

    def draw_widgets(self):
        self.sample_username_label.grid(row=0, column=0, sticky=W, padx=10, pady=1)
        self.sample_info_username_label.grid(row=0, column=1, sticky=W)

        self.info_username_label.grid(row=1, column=0, sticky=W, padx=10, pady=1)
        self.username_entry.grid(row=1, column=1, sticky=W + E)
        self.valid_username_label.grid(row=1, column=2, sticky=W)

        self.sample_age_label.grid(row=2, column=0, sticky=W, padx=10, pady=1)
        self.sample_info_age_label.grid(row=2, column=1, sticky=W)

        self.info_age_label.grid(row=3, column=0, sticky=W, padx=10, pady=1)
        self.age_entry.grid(row=3, column=1, sticky=W + E)
        self.valid_age_label.grid(row=3, column=2, sticky=W)

    def run(self):
        self.get_user()
        self.get_age()
        self.draw_widgets()
        self.mainloop()


if __name__ == '__main__':
    person = User()
    person.run()
