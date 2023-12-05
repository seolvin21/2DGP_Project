import random
from pico2d import *

import game_framework
import loading_mode


class Background:
    def __init__(self):
        bg_list = ['factory', 'neonsigns']
        self.bg = random.choice(bg_list)
        self.back_image = load_image('./background/BG_1_1.png')

        self.building_image = load_image('./background/BG_base_1_1.png')
        self.cloud_image = load_image('./background/BG_cloud_1_3.png')

        self.cloud_image2 = load_image('./background/BG_cloud_1_1.png')
        self.signs = load_image('./background/BG_mid_sign_1_7.png')
        self.low_building = load_image('./background/BG_low_building_11_10.png')
        self.low_building2 = load_image('./background/BG_low_building_12_9.png')

        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

    def draw(self):
        self.back_image.draw(400, 300)
        self.building_image.draw(400, 300, 800, 600)

        if self.bg == 'factory':
            self.cloud_image.draw(400, 300, 800, 600)
        elif self.bg == 'signs':
            self.cloud_image2.draw(400, 300, 800, 600)
            self.low_building.draw(100, 200)
            self.low_building2.draw(700, 200)
            self.signs.draw(600,100)

    def update(self):
        pass

class StartScreen:
    def __init__(self):
        self.image = load_image('gamestart.png')

        self.font = load_font('neodgm_code.ttf', 40)

        self.bgm = load_music('./sound/cyberpunk_city_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.play_bgm = load_music('./sound/play_mode_bgm.mp3')
        self.play_bgm.set_volume(64)

        StartScreen.select_sound = load_wav('./sound/select.wav')
        StartScreen.select_sound.set_volume(64)

        self.loading_time = get_time()

    def draw(self):
        self.image.draw(400, 300)
        self.font.draw(500, 440, f'PRESS ANY KEY', (255, 0, 255))
        self.font.draw(498, 438, f'PRESS ANY KEY', (255, 255, 255))

    def update(self):
        pass

    def handle_event(self, event):
        if (event.type) == (SDL_KEYDOWN):
            StartScreen.select_sound.play()
            self.play_bgm.repeat_play()
            game_framework.change_mode(loading_mode)