import random
from pico2d import *

import game_framework
import loading_mode


class Background:
    def __init__(self):
        bg_list = ['factory']
        self.bg = random.choice(bg_list)
        self.back_image = load_image('./background/BG_1_1.png')
        self.building_image = load_image('./background/BG_base_1_1.png')
        self.cloud_image = load_image('./background/BG_cloud_1_3.png')

        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

    def draw(self):
        if self.bg == 'factory':
            self.back_image.draw(400, 300)
            self.building_image.draw(400, 300, 800, 600)
            self.cloud_image.draw(400, 300, 800, 600)

    def update(self):
        pass

class StartScreen:
    def __init__(self):
        self.image = load_image('gamestart.png')

        self.bgm = load_music('./sound/cyberpunk_city_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        StartScreen.select_sound = load_wav('./sound/select.wav')
        StartScreen.select_sound.set_volume(32)

        self.loading_time = get_time()

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            StartScreen.select_sound.play()
            game_framework.change_mode(loading_mode)
