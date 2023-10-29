from pico2d import load_image

class Background:
    def __init__(self):
        self.image = load_image('background\\BG_1_1.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass