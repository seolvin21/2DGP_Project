from pico2d import load_image
import game_world
from shared import Shared

class Game_Start:
    def __init__(self):
        self.image = load_image('gamestart.jpg')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        if not Shared.isstart:
            game_world.remove_object(self)