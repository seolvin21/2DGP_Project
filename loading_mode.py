from pico2d import *

import end_mode
import game_framework
import minigame_mode
import play_mode
import server

def init():
    global image
    global running
    global loading_time

    running = True

    image = load_image('cyberpunk.png')
    loading_time = get_time()
    server.stage += 1

def finish():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    global running

    if get_time() - loading_time >= 2.0:
        if server.stage >= 6:   # until stage 5
            game_framework.change_mode(end_mode)
        else:
            game_framework.change_mode(minigame_mode)
        running = False


def handle_events():
    events = get_events()
