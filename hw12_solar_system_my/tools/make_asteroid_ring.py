from random import uniform, random, randint

from hw12_solar_system_my.classes.planet import Planet
from hw12_solar_system_my.dto.planet import PlanetData


def make_aster_data():
    """Asteroid data"""
    asteroids_data = {}
    for number_aster in range(300):
        aster = PlanetData((uniform(0.05, 0.2), uniform(0.05, 0.2)),
                           (random(), random(), random()),
                           randint(400, 1000), randint(350, 600),
                           uniform(0.001, 0.04))

        asteroids_data['aster_' + str(number_aster)] = aster
    return asteroids_data


def make_aster_data_saturn():
    """Asteroid data"""
    asteroids_data_saturn = {}
    for number_aster in range(200):
        aster_saturn = PlanetData((uniform(0.001, 0.01), uniform(0.05, 0.1)),
                                  (random(), random(), random()),
                                  randint(20, 25), randint(25, 40),
                                  uniform(0.001, 0.04))

        asteroids_data_saturn['aster_saturn' + str(number_aster)] = aster_saturn
    print(asteroids_data_saturn)
    return asteroids_data_saturn


def make_asteroids(star=None):
    """Make asteroids of solar system"""
    asteroids_data = make_aster_data()
    asters = []
    for asteroid in asteroids_data:
        asters.append(Planet(asteroids_data[asteroid], star))
    return asters


def make_asteroids_saturn(star=None):
    """Make asteroids of solar system"""
    asteroids_data_saturn = make_aster_data_saturn()
    asters_saturn = []
    for asteroid in asteroids_data_saturn:
        asters_saturn.append(Planet(asteroids_data_saturn[asteroid], star))
    print(asters_saturn)
    return asters_saturn
