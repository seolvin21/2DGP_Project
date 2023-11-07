from pico2d import *

import game_world
from mario import Mario
from shared import Shared


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            mario.handle_event(event)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def init():
    global running
    global gamestart
    global mario

    running = True


def finish():
    pass


def update():
    game_world.update()