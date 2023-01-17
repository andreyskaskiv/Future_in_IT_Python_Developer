import os
from pathlib import Path
from turtle import Screen

from hw13_turtle_game import picture

PATH_TO_PIC = Path(picture.__file__).parent


class Window:
    WIDTH = 800
    HEIGHT = 600
    WIDTH_HALF = WIDTH // 2
    HEIGHT_HALF = HEIGHT // 2

    def __init__(self, screen_title: str = 'Turtle go go go.... '):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.WIDTH, self.HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.bgpic(os.path.join(PATH_TO_PIC, 'sea.png'))
        self.canvas.listen()
        self.canvas.tracer(0)
        self.canvas.delay()


class WindowEND:
    WIDTH = 600
    HEIGHT = 400
    WIDTH_HALF = WIDTH // 2
    HEIGHT_HALF = HEIGHT // 2

    def __init__(self, screen_title: str = 'Game over'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.WIDTH, self.HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.bgpic(os.path.join(PATH_TO_PIC, 'wasted.png'))
        self.canvas.listen()
        self.canvas.tracer(0)
