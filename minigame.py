import random

from pico2d import *

arrow_names = ['arrow_']
class Minigame:
    images = []

    def __init__(self):
        # arrows = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.input_list = []
        self.arrow_list = [random.randint(1,4) for _ in range(random.randint(5,10))]
        self.input_time = get_time()
        self.font = load_font('NanumSquareEB.ttf', 30)
        self.result = None
        self.a = 80

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
        if get_time() - self.input_time >= 3.0 and self.input_list != self.arrow_list:
            self.result = 'BAD'
        elif self.input_list != self.arrow_list and len(self.input_list) >= len(self.arrow_list):
            self.result = 'BAD'
        else:
            if self.input_list == self.arrow_list:
                self.result = 'GOOD'
        pass

    def draw(self):
        self.font.draw(400, 580, f'Remaining Time: {get_time() - self.input_time:.0f}', (255, 255, 255))

        for i in range(len(self.input_list)):
            input_arrow_image = load_image('./arrows/arrow_' + str(self.input_list[i]) + '.png')
            input_arrow_image.draw(200 + (self.a * i), 300, 50, 50)
            self.font.draw(400 + (self.a * i), 520, f'{self.input_list[i]}', (255, 255, 255))

        for i in range(len(self.arrow_list)):
            arrow_image = load_image('./arrows/arrow_' + str(self.arrow_list[i]) + '.png')
            arrow_image.draw(200 + (self.a * i), 500, 50, 50)
            self.font.draw(400 + (self.a * i), 550, f'{self.arrow_list[i]}', (255, 255, 255))

        if self.result == 'BAD':
            self.font.draw(400, 300, f'BAD', (255, 255, 255))

        elif self.result == 'GOOD':
            self.font.draw(400, 300, f'GOOD', (255, 255, 255))

        # self.font.draw(400, 300, f'PERFECT', (255, 255, 255), 400, 400)