from pico2d import *

import game_world
from background import Background
from mario import Mario
from game_start import Game_Start
from shared import Shared

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Shared.isstart = False
        else:
            mario.handle_event(event)

def reset_world():
    global running
    global gamestart
    global mario

    running = True

    game_start = Game_Start()
    game_world.add_object(game_start, 2)

    game_running = Background()
    game_world.add_object(game_running, 0)

    mario = Mario()

def update_world():
    game_world.update()
    if not Shared.isstart:
        print("Game is running")

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


isstart = True
open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
