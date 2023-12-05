import random

from pico2d import *

import game_framework
import loading_mode
import mini_loading_mode
import server

arrow_names = ['arrow_']
class Minigame:
    images = []


    def __init__(self):
        # arrows = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.input_list = []
        self.arrow_list = [random.randint(1,4) for _ in range(random.randint(9,10))]
        self.input_time = get_time()
        self.font = load_font('neodgm_code.ttf', 30)
        self.breathe_font = load_font('neodgm_code.ttf', 50)
        self.result = None
        self.space = 70
        self.bg = load_image('minigame.png')
        self.time_limit = 5.0
        self.elapsed_time = 0.0
        self.remaining_time = self.time_limit

    def change_mode(self):
        server.game_result = self.result
        print(server.game_result)
        game_framework.change_mode(mini_loading_mode)

    def handle_event(self, event):
        if len(self.input_list) < len(self.arrow_list):
            if event.key == SDLK_LEFT:
                self.input_list.append(2)
            elif event.key == SDLK_RIGHT:
                self.input_list.append(4)
            elif event.key == SDLK_UP:
                self.input_list.append(3)
            elif event.key == SDLK_DOWN:
                self.input_list.append(1)

    def update(self):
        self.elapsed_time += game_framework.frame_time
        self.remaining_time = max(self.time_limit - self.elapsed_time, 0)

        if get_time() - self.input_time >= 5.0 and self.input_list != self.arrow_list:
            self.result = 'FAILED'
            self.change_mode()
        elif self.input_list != self.arrow_list and len(self.input_list) >= len(self.arrow_list):
            self.result = 'FAILED'
            self.change_mode()
        else:
            if self.input_list == self.arrow_list:
                self.result = 'SUCCESS'
                self.change_mode()

    def draw(self):
        self.bg.draw(400, 300)
        self.breathe_font.draw(270, 300, f'심호흡하자!', (255, 255, 255))

        self.font.draw(552, 578, f'REMAINIG TIME: {self.remaining_time:.0f}', (0, 255, 255))
        self.font.draw(550, 580, f'REMAINIG TIME: {self.remaining_time:.0f}', (255, 255, 255))

        for i in range(len(self.input_list)):
            input_arrow_image = load_image('./arrows/p_arrow_' + str(self.input_list[i]) + '.png')
            input_arrow_image.draw(110 + (self.space * i), 100, 70, 70)
            # self.font.draw(400 + (self.space * i), 520, f'{self.input_list[i]}', (255, 255, 255))

        for i in range(len(self.arrow_list)):
            arrow_image = load_image('./arrows/arrow_' + str(self.arrow_list[i]) + '.png')
            arrow_image.draw(100 + (self.space * i), 200, 70, 70)
            # self.font.draw(400 + (self.space * i), 550, f'{self.arrow_list[i]}', (255, 255, 255))

        if self.result == 'BAD':
            self.font.draw(400, 300, f'BAD', (255, 255, 255))

        elif self.result == 'GOOD':
            self.font.draw(400, 300, f'GOOD', (255, 255, 255))
        # self.font.draw(400, 300, f'PERFECT', (255, 255, 255), 400, 400)