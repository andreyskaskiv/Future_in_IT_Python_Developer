import os
from pathlib import Path

import winsound

from hw13_turtle_game import sound

PATH_TO_SOUNDS = Path(sound.__file__).parent


class Sound:
    @staticmethod
    def play_victory():
        winsound.PlaySound(os.path.join(PATH_TO_SOUNDS, 'the_sound_of_victory.wav'), winsound.SND_ASYNC)

    @staticmethod
    def play_collision():
        winsound.PlaySound(os.path.join(PATH_TO_SOUNDS, 'inecraft_death.wav'), winsound.SND_ASYNC)

    @staticmethod
    def play_background():
        winsound.PlaySound(os.path.join(PATH_TO_SOUNDS, 'inecraft_style.wav'), winsound.SND_ASYNC)

