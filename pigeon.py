import random
import math

from pico2d import *
import game_world
import game_framework
import server

# Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = random.randint(50, 100)
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
        self.x, self.y = random.choice([0, 800]), random.randint(150, 500)
        Pigeon.image = load_image('pigeon_spritesheet.png')
        self.frame = 0
        if self.x <= 10:
            self.dir = 1
        elif self.x >= 730:
            self.dir = -1
        self.action = 0
        self.wid, self.hgt = 80, 100
        self.collided = False

        min_hgt = 40  # 최소 폭
        max_hgt = 70  # 최대 폭

        self.hgt_size = random.randint(min_hgt, max_hgt)
        self.wid_size = self.hgt_size - 20

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if not self.collided:
            if self.dir == 1 and self.x > 750 or self.dir == -1 and self.x < 10:
                self.__init__()
    def draw(self):
        if self.dir > 0:
            self.image.clip_composite_draw(int(self.frame) * self.wid, self.action * self.hgt,
                                           self.wid, self.hgt, 0, 'h', self.x, self.y, self.wid_size, self.hgt_size)
        else:
            self.image.clip_draw(int(self.frame) * self.wid, self.action * self.hgt,
                                 self.wid, self.hgt, self.x, self.y, self.wid_size, self.hgt_size)
        # draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def get_bb(self):
        return (self.x - self.wid_size / 2, self.y - self.hgt_size / 2,
                self.x + self.wid_size / 2, self.y + self.hgt_size / 2)

    def handle_collision(self, group, other):
        if group == 'player:pigeon':
            print('collision:', self.x, self.y)
            self.collided = True
            self.__init__()
