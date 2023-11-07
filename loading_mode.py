from pico2d import *


def handle_events():
    events = get_events()


def init():
    global image
    global running
    global loading_time

    running = True

    image = load_image('cyberpunk.png')
    loading_time = get_time()


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def finish():
    pass


def update():
    global running
    if get_time() - loading_time >= 2.0:
        running = False