from tkinter import *

from hw14_Tk_Person.person_class.age_class import Age
from hw14_Tk_Person.person_class.username_class import UserName
from hw14_Tk_Person.base_classes.window_class import Window


class MainApp:
    def __init__(self):
        # self.user = UserName()
        self.age = Age()


    def run(self):
        self.draw_widgets()
        self.age.mainloop()

    def draw_widgets(self):
        # self.user.sample_username_label.grid(row=0, column=0, sticky=W, padx=10, pady=1)
        # self.user.sample_info_username_label.grid(row=0, column=1, sticky=W)
        #
        # self.user.info_username_label.grid(row=1, column=0, sticky=W, padx=10, pady=1)
        # self.user.username_entry.grid(row=1, column=1, sticky=W + E)
        # self.user.valid_username_label.grid(row=1, column=2, sticky=W)


        self.age.sample_age_label.grid(row=2, column=0, sticky=W, padx=10, pady=1)
        self.age.sample_info_age_label.grid(row=2, column=1, sticky=W)

        self.age.info_age_label.grid(row=3, column=0, sticky=W, padx=10, pady=1)
        self.age.age_entry.grid(row=3, column=1, sticky=W + E)
        self.age.valid_age_label.grid(row=3, column=2, sticky=W)


if __name__ == '__main__':
    person = MainApp()
    person.run()


