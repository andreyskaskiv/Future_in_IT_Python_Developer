from hw13_turtle_game.base_classes.text import Text
from hw13_turtle_game.base_classes.window import Window


class Level(Text):
    """Auto-creating object level notes"""
    FONT = ("Arial", 22, "normal")  # font=("Arial", 8, 'normal', 'bold', 'italic', 'underline')

    def __init__(self):
        super().__init__()
        self.color('black')
        self.__level = 0
        self.setposition(-Window.WIDTH_HALF + 20, Window.HEIGHT_HALF - 40)

    def show_value(self):
        return self.write(f"Level: {self.__level}", font=self.FONT)

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level += level


class Life(Text):
    """Auto-creating object life notes"""
    FONT = ("Arial", 28, "bold")  # font=("Arial", 8, 'normal', 'bold', 'italic', 'underline')

    def __init__(self):
        super().__init__()
        self.color('red')
        self.__life = 3
        self.setposition(Window.WIDTH_HALF - 145, Window.HEIGHT_HALF - 50)

    def show_value(self):
        return self.write(f"Life: {self.__life}", font=self.FONT)

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life: int):
        self.__life -= life


class Player(Text):
    """Auto-creating object player notes"""
    FONT = ("Arial", 22, "bold")  # font=("Arial", 8, 'normal', 'bold', 'italic', 'underline')

    def __init__(self, player=None):
        super().__init__()
        self.color('black')
        self.__player = player
        self.setposition(-Window.WIDTH_HALF + 20, Window.HEIGHT_HALF - 80)

    def show_value(self):
        return self.write(f"Player: {self.__player}", font=self.FONT)

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player: int):
        self.__player = player


class GameOver(Text):
    """Auto-creating object gameover notes"""
    FONT = ("Arial", 22, "bold")  # font=("Arial", 8, 'normal', 'bold', 'italic', 'underline')

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.setposition(-Window.WIDTH_HALF // 2, Window.HEIGHT_HALF // 5)


