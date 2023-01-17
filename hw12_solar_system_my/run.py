import os
from pathlib import Path
from turtle import *
from typing import List

from hw12_solar_system_my import picture
from hw12_solar_system_my.classes.planet import Planet
from hw12_solar_system_my.tools.make_asteroid_ring import make_asteroids, make_asteroids_saturn
from hw12_solar_system_my.tools.make_planet import make_planets
from hw12_solar_system_my.tools.make_stars import run_stars

PATH_TO_PIC = Path(picture.__file__).parent.absolute()


def make_window():
    """Make window instance and settings"""
    screen = Screen()
    screen.title('Solar system')
    screen.setup(width=0.9, height=0.9)
    screen.bgpic(os.path.join(PATH_TO_PIC, 'win11.png'))
    screen.cv._rootwindow.resizable(False, False)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_base_planet():
    """Make base central planet"""
    base_planet = Turtle(shape='circle')
    base_planet.color('yellow')
    base_planet.shapesize(4, 4)
    return base_planet


def check_distance(asteroids: List[Planet]):
    for i in range(len(asteroids)):
        for j in range(i + 1, len(asteroids)):
            if asteroids[i].distance(asteroids[j]) < 10:
                asteroids[i].increase_angle, asteroids[j].increase_angle = \
                    asteroids[j].increase_angle, asteroids[i].increase_angle


def move_objects(objects):
    """Move stars"""
    for obj in objects:
        obj.move()


def mainloop():
    """Mainloop of Solar system app"""
    while True:
        move_objects(stars)

        move_objects(asters)
        check_distance(asters)

        move_objects(asters_saturn)
        check_distance(asters_saturn)

        window.update()


if __name__ == '__main__':
    window = make_window()
    window.onclick(run_stars)

    sun = make_base_planet()
    stars, saturn = make_planets(sun)
    asters = make_asteroids(sun)
    asters_saturn = make_asteroids_saturn(saturn)

    mainloop()
