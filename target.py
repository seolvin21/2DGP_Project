from pico2d import *
import game_framework
import game_world


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

# bullet animation speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

animation_names = ['skill_bullet_1_']

class Boom:
    images = None

    def load_images(self):
        if Boom.images == None:
            Boom.images = {}
            for name in animation_names:
                Boom.images[name] = [load_image("./explosion/" + name + "%d" % i + ".png") for i in range(1, 8)]

    def __init__(self, target):
        self.target = target
        self.load_images()
        self.frame = 0
        self.x, self.y = self.target.x, self.target.y

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.frame > 7:
            game_world.remove_object(self)

    def draw(self):
        frame_index = int(self.frame)
        if 0 <= frame_index < len(Boom.images['skill_bullet_1_']):
            Boom.images['skill_bullet_1_'][int(self.frame)].draw(self.x, self.y, 200, 200)