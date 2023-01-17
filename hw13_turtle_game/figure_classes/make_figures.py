from random import randint, random

from hw13_turtle_game.base_classes.sprite import Sprite
from hw13_turtle_game.base_classes.window import Window


class Figure(Sprite):
    """Describes the properties of the square"""
    size = 20

    def __init__(self, figure):
        super().__init__(figure)
        self.color(self.generate_color())
        self.goto(self.get_random_position())
        self.shapesize(stretch_wid=1, stretch_len=randint(2, 5))
        self.showturtle()
        self.delta_x = 0
        self.delta_y = 0

    def move(self):
        self.goto(self.xcor() - self.delta_x, self.ycor() + self.delta_y)

    @staticmethod
    def generate_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        x = randint(Window.WIDTH_HALF, 10 * Window.HEIGHT)
        y = randint(-Window.HEIGHT_HALF + 100, Window.HEIGHT_HALF - 100)
        return x, y


class FigureTurtle(Sprite):
    """Describes the properties of the turtle"""
    size = 20

    def __init__(self, figure):
        super().__init__(figure)
        self.color('black')
        self.goto(self.get_random_position())
        self.left(90)
        self.shapesize(1.3)
        self.showturtle()
        self.delta_x = 0
        self.delta_y = 0

    def move(self):
        self.goto(self.xcor() + self.delta_x, self.ycor() + self.delta_y)

    def move_up(self):
        y = self.ycor() + 10
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 10
        self.sety(y)

    def move_left(self):
        x = self.xcor() - 10
        self.setx(x)

    def move_right(self):
        x = self.xcor() + 10
        self.setx(x)

    @staticmethod
    def get_random_position():
        x = randint(-100, 100)
        y = -Window.HEIGHT_HALF + 20
        return x, y



