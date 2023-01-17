from hw12_solar_system_my.classes.planet import Planet
from hw12_solar_system_my.dto.planet import PlanetData


def make_planets_data():
    """Planet data"""
    mercury = PlanetData((0.5, 0.5), 'grey', 55, 70, 0.02)
    venus = PlanetData((0.5, 0.5), 'bisque', 75, 80, 0.02)
    earth = PlanetData((1.0, 1.0), 'deepskyblue', 120, 140, -0.02)
    moon = PlanetData((0.4, 0.4), 'grey', 20, 20, 0.08)
    mars = PlanetData((0.8, 0.8), 'red', 160, 180, 0.007)
    phobos = PlanetData((0.3, 0.3), 'grey', 30, 30, 0.06)
    deimos = PlanetData((0.2, 0.2), 'white', 20, 20, 0.08)
    jupiter = PlanetData((2.2, 2.2), 'coral', 200, 220, 0.005)
    saturn = PlanetData((1.5, 1.5), 'orange', 240, 280, 0.005, 'saturn')
    uranus = PlanetData((1.8, 1.8), 'dodgerblue', 300, 320, 0.005)
    neptune = PlanetData((1.5, 1.5), 'mediumblue', 340, 360, 0.007)
    pluto = PlanetData((0.5, 0.5), 'lightgrey', 380, 400, 0.007)

    stars_data = {
        'mercury': mercury,
        'venus': venus,
        'earth': earth,
        'moon': moon,
        'mars': mars,
        'phobos': phobos,
        'deimos': deimos,
        'jupiter': jupiter,
        'saturn': saturn,
        'uranus': uranus,
        'neptune': neptune,
        'pluto': pluto,
    }
    return stars_data


def make_planets(base_star=None):
    """Make planets of solar system"""
    planets_data = make_planets_data()
    mercury = Planet(planets_data['mercury'], base_star)
    venus = Planet(planets_data['venus'], base_star)
    earth = Planet(planets_data['earth'], base_star)
    moon = Planet(planets_data['moon'], earth)
    mars = Planet(planets_data['mars'], base_star)
    phobos = Planet(planets_data['phobos'], mars)
    deimos = Planet(planets_data['deimos'], mars)
    jupiter = Planet(planets_data['jupiter'], base_star)
    saturn = Planet(planets_data['saturn'], base_star)
    uranus = Planet(planets_data['uranus'], base_star)
    neptune = Planet(planets_data['neptune'], base_star)
    pluto = Planet(planets_data['pluto'], base_star)
    planets = [mercury, venus, earth, moon, mars, phobos, deimos, jupiter, saturn, uranus, neptune, pluto]
    return planets, saturn
