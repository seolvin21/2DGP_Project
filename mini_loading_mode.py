from pico2d import *

import end_mode
import game_framework
import play_mode
import server

def init():
    global success_image, failed_image
    global success_sound, failed_sound
    global running
    global loading_time

    running = True

    success_image = load_image('cyberpunk.png')
    success_sound = load_wav('./sound/mini_success.wav')
    success_sound.set_volume(64)
    failed_image = load_image('cyberpunk.png')
    failed_sound = load_wav('./sound/mini_failed.wav')
    failed_sound.set_volume(16)

    loading_time = get_time()

def finish():
    pass


def draw():
    clear_canvas()
    if server.game_result == 'SUCCESS':
        success_sound.play()
        success_image.draw(400, 300, 1010, 385)
    elif server.game_result == 'FAILED':
        failed_sound.play()
        failed_image.draw(400, 300, 1010, 385)
    update_canvas()


def update():
    global running

    if get_time() - loading_time >= 2.0:
        game_framework.change_mode(play_mode)
        running = False


def handle_events():
    events = get_events()
