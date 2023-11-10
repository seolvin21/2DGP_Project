import random

from pico2d import *
import game_framework

import game_world
from target import Target
from background import Background
from participant import Player
from pigeon import Pigeon


# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            targeting.handle_event(event)
            player.handle_event(event)

def init():
    global bg
    global player
    global targeting

    running = True

    bg = Background()
    game_world.add_object(bg, 0)

    player = Player()
    game_world.add_object(player, 1)

    global pigeons
    pigeons = [Pigeon() for _ in range(5)]
    game_world.add_objects(pigeons, 1)

    targeting = Target()
    game_world.add_object(targeting, 2)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

