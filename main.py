from pico2d import *
import game_framework

import minigame_mode as starting_mode

open_canvas()
hide_cursor()
game_framework.run(starting_mode)
close_canvas()
