from math import sin, cos
from random import randint

from hw12_solar_system_my.classes.sprite import Sprite


class Planet(Sprite):
    def __init__(self, obj, star):
        Sprite.__init__(self)
        print(self)
        self.up()
        self.shapesize(*obj.planet_size)
        self.color(obj.planet_color)
        self.name = obj.name
        self.x = 0
        self.y = 0
        self.angle = randint(0, 360)
        self.increase_angle = obj.increase_angle
        self.radius_major = obj.radius_major
        self.radius_minor = obj.radius_minor

        self.star = star

    def move(self):
        """Move planets"""
        self.x = self.radius_major * cos(self.angle)
        self.y = self.radius_minor * sin(self.angle)

        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle
