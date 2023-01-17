from random import randint, random, choice
from turtle import Turtle


def make_obj_text():
    """Make object text"""
    text = Turtle(visible=False)
    text.color('white')
    text.penup()
    text.setposition(400, -400)
    return text


def counter_stars(func):
    """Counting the stars"""
    counter = 0
    text = make_obj_text()

    def wrapper(*args, **kwargs):
        nonlocal counter
        result = func(*args, **kwargs)
        counter += 1
        text.clear()
        text.write(f'Quantity of stars created = {counter}', font=("Arial", 20))
        return result

    return wrapper


@counter_stars
def make_obj_star(x, y):
    """Make object star"""
    obj_star = Turtle()
    obj_star.hideturtle()
    obj_star.color((random(), random(), random()))
    obj_star.up()
    obj_star.setposition(x, y)
    obj_star.down()
    return obj_star


def make_stars(star, corner, size):
    """Draw a star"""
    if corner % 2 != 0:
        for _ in range(corner):
            star.forward(size)
            angle = corner // 2 * 360 / corner
            star.left(angle)


def filling_star(star, corner, size):
    """Object fill"""
    star.left(randint(1, 10))
    star.begin_fill()
    make_stars(star, corner, size)
    star.end_fill()


def move_star(star):
    """Set the size and quantity of corners of the object"""
    star_size = randint(5, 30)
    angle_quantity = choice([5, 7, 9, 11])
    filling_star(star, angle_quantity, star_size)


def run_stars(x, y):
    star = make_obj_star(x, y)
    move_star(star)
