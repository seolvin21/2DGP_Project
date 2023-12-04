from pico2d import *
import game_framework
import game_world
import loading_mode
from background import StartScreen


def init():
    global bg

    bg = StartScreen()
    game_world.add_object(bg, 0)


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            bg.handle_event(event)
    pass
