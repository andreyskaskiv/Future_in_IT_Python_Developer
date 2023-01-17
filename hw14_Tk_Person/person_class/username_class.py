from tkinter import *
from string import ascii_lowercase, ascii_uppercase

from hw14_Tk_Person.base_classes.window_class import Window


class UserName(Window):
    __ALPHABET_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    __ALPHABET_UPPER_UA = __ALPHABET_UA.upper()

    def __init__(self):
        super().__init__()
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
