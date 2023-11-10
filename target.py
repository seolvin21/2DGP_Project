from pico2d import *

class Target:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('Target.png')
        self.wid, self.hgt = 100, 100

    def handle_event(self, event):
       if event.type == SDL_MOUSEMOTION:
           self.x, self.y = event.x, 600 - 1 - event.y
       elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
           print(self.x, self.y)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.wid, self.hgt)