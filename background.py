from pico2d import load_image

class Background:
    def __init__(self):
        self.back_image = load_image('./background/BG_1_1.png')
        self.building_image = load_image('./background/BG_base_1_1.png')
        self.cloud_image = load_image('./background/BG_cloud_1_3.png')
    def draw(self):
        self.back_image.draw(400, 300)
        self.building_image.draw(400, 300, 800, 600)
        self.cloud_image.draw(400, 300, 800, 600)

    def update(self):
        pass