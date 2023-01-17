from turtle import Turtle


class Text(Turtle):
    """Base text"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
