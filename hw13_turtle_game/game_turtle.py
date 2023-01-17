import time
from datetime import datetime

from hw13_turtle_game.base_classes.window import Window
from hw13_turtle_game.figure_classes.make_figures import FigureTurtle, Figure
from hw13_turtle_game.game_notes.notes import Level, Life, Player, GameOver
from hw13_turtle_game.sounds_handlers.game_sounds import Sound

START_GAME = datetime.now()


class Game:
    __figures_qty = 100

    def __init__(self, gamer=None):
        self.window = Window()

        self.figures = self.make_figures(self.__figures_qty)
        self.sammy = FigureTurtle('turtle')
        self.grade = Level()
        self.life = Life()
        self.game_sounds = Sound()
        self.player = Player(gamer)
        self.statistic = GameOver()

    def run(self):
        self.game_sounds.play_background()

        for figure in self.figures:
            figure.delta_x = 1

        while True:
            for figure in self.figures:
                figure.move()
                self.check_border(figure)
            self.sammy.move()
            self.check_border_sea(self.sammy)
            self.check_collision()

            self.grade.clear()
            self.grade.show_value()
            self.life.clear()
            self.life.show_value()
            self.player.clear()
            self.player.show_value()

            if self.life.life == 0:
                for figure in self.figures:
                    figure.hideturtle()
                self.sammy.hideturtle()
                self.window.canvas.update()
                self.message(self.statistic, self.player.player)
                self.window.canvas.update()
                self.window.canvas.ontimer(self.fun())

            self.window.canvas.onkeypress(self.sammy.move_up, "Up")
            self.window.canvas.onkeypress(self.sammy.move_down, "Down")
            self.window.canvas.onkeypress(self.sammy.move_left, "Left")
            self.window.canvas.onkeypress(self.sammy.move_right, "Right")

            self.window.canvas.update()

    @staticmethod
    def message(statistic, player):
        END_GAME = datetime.now()
        dtime = END_GAME - START_GAME
        GAME_OVER_MSG = f'Game over!\n' \
                        f'Game time  {dtime}\n' \
                        f'Player name: {player}'
        statistic.write(GAME_OVER_MSG, font=("Arial", 22, "bold"))

    @staticmethod
    def fun():
        print('Game over!')
        time.sleep(2)
        exit()

    def check_collision(self):
        for i in range(len(self.figures)):
            if self.figures[i].distance(self.sammy) < 25:
                self.game_sounds.play_collision()
                self.sammy.goto(self.sammy.get_random_position())
                self.life.life = 1
                # self.figures[i].delta_x, self.sammy.delta_x = self.sammy.delta_x, self.figures[i].delta_x
                # self.figures[i].delta_y, self.sammy.delta_y = self.sammy.delta_y, self.figures[i].delta_y

    def check_border(self, figure):
        x = figure.xcor()
        if x < -self.window.WIDTH_HALF - 50:
            figure.goto(figure.get_random_position())

    def check_border_sea(self, sammy):
        y = sammy.ycor()
        if y > self.window.WIDTH_HALF - 180:
            self.grade.level = 1
            self.game_sounds.play_victory()
            sammy.goto(sammy.get_random_position())

    @staticmethod
    def make_figures(qty: int):
        return [Figure('square') for _ in range(qty)]


def main(player):
    gamer = player.get()
    game = Game(gamer)
    game.run()

# if __name__ == '__main__':
#     game = Game()
#     game.run()
