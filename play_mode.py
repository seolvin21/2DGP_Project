import random

from pico2d import *
import game_framework

import game_world
from target import Target, Boom
from background import Background
from participant import Player
from pigeon import Pigeon



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

            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                if targeting.x >= player.x - 200 and targeting.x <= player.x + 200:
                    boom = Boom(targeting)
                    game_world.add_object(boom, 1)

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

    targeting = Target()
    game_world.add_object(targeting, 2)


def finish():
    game_world.clear()
    pass

# Define the pigeon spawn interval in seconds
PIGEON_SPAWN_INTERVAL = 2.0
# Initialize the pigeon spawn timer
pigeon_spawn_timer = 0.0

def update():
    global pigeon_spawn_timer

    # Update the timer
    pigeon_spawn_timer += game_framework.frame_time

    # Check if it's time to spawn a new pigeon
    if pigeon_spawn_timer >= PIGEON_SPAWN_INTERVAL:
        # Spawn a new pigeon
        pigeon = Pigeon()
        game_world.add_object(pigeon, 1)

        # Reset the timer
        pigeon_spawn_timer = 0.0

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

