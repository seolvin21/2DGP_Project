from pico2d import *

import game_framework
import play_mode




def init():
    global image
    global running
    global loading_time

    running = True

    image = load_image('cyberpunk.png')
    loading_time = get_time()

def finish():
    pass

def draw():
    clear_canvas()
    image.draw(400,300, 1010, 385)
    update_canvas()

def update():
    global running
    if get_time() - loading_time >= 2.0:
        clear_canvas()
        game_framework.change_mode(play_mode)
        running = False


def handle_events():
    events = get_events()
