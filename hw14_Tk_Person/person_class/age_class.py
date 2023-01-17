from tkinter import *
from string import ascii_lowercase, ascii_uppercase

from hw14_Tk_Person.base_classes.window_class import Window


class Age(Window):
    __AGE_MIN = 16
    __AGE_MAX = 66

    def __init__(self):
        super().__init__()

        self.age = StringVar()
        self.check_age = StringVar()

        self.sample_age_label = Label(self, text="Вік в діапазоні: ",
                                      bg=self.bg_all,
                                      justify=LEFT,
                                      font=("Arial", 16))

        self.sample_info_age_label = Label(self, text=f"от {Age.__AGE_MIN} до {Age.__AGE_MAX}",
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

    def check_age_input(self, *args):
        age = self.age.get()
        for number in age:
            if not number.isdigit():
                return self.check_age.set('only digit')

        age = int(age)
        if age < self.__AGE_MIN or age > self.__AGE_MAX:
            return self.check_age.set("Вік не у діапазоні")
        return self.check_age.set("✔")
