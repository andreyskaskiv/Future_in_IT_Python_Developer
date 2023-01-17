from tkinter import *
from hw13_turtle_game.game_turtle import main

class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        print(self.__class__)

        self.title('Connect...')
        self['bg'] = '#FFFFE0'
        self.resizable(width=False, height=False)

        Label(self, text="Let's play?", font="Arial 22", bg='#FFFFE0').pack(side=TOP)

        Button(self, width=10, height=1,
               text="Yes",
               bg='#FAFAD2',
               borderwidth=8,
               command=self.show_next_window,
               font=("Comic Sans MS", 12, "bold")).pack(side=LEFT)
        Button(self, width=10, height=1,
               text="No...",
               bg='#FAFAD2',
               borderwidth=8,
               fg="red",
               command=quit,
               font=("Comic Sans MS", 12, "bold")).pack(side=LEFT)

    def show_next_window(self):
        self.destroy()
        WindowPlayer().mainloop()


class WindowPlayer(Tk):

    def __init__(self, *arg, **kwarg):
        print(self.__class__)
        super().__init__(*arg, **kwarg)


        self.title('Player')
        self['bg'] = '#E6E6FA'
        self.geometry('500x115+300+300')
        self.resizable(width=False, height=False)
        self.player_name = StringVar()

        Label(self, text="Enter player name:", font="Arial 22", bg='#E6E6FA').pack(side=TOP)

        Entry(self, textvariable=self.player_name, width=30,
              bg='#FFFFE0',
              borderwidth=6,
              font=("Comic Sans MS", 12, "bold")).pack(side=TOP)

        Button(self, width=10, height=1,
               text="Ok",
               bg='#FFEFD5',
               borderwidth=5,
               command=self.show_next_window,
               font=("Comic Sans MS", 12, "bold")).pack()

    def show_next_window(self):
        self.destroy()
        main(self.player_name)


if __name__ == '__main__':
    MainApp().mainloop()
