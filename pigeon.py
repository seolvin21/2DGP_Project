import random

from pico2d import *
import game_world
import game_framework

# Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

class Pigeon:
    image = None
    def __init__(self):
        self.x, self.y = 80, 300
        Pigeon.image = load_image('pigeon_spritesheet.png')
        self.frame = 0
        self.dir = 1
        self.wid, self.hgt = 80, 100
        self.action = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 750:
            self.dir = -1
        elif self.x < 10:
            self.dir = 1
        self.x = clamp(10, self.x, 800)

    def draw(self):
        if self.dir > 0:
            self.image.clip_composite_draw(int(self.frame)*self.wid, self.action*self.hgt,
                                           self.wid, self.hgt,0, 'h',  self.x, self.y, 80, 100)
        else:
            self.image.clip_draw(int(self.frame) * self.wid, self.action * self.hgt,
                                 self.wid, self.hgt, self.x, self.y, self.wid, self.hgt)
    def handle_event(self, event):
        pass