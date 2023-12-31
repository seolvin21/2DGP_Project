from pico2d import *
import game_framework
import game_world
import loading_mode
import play_mode
import server


def leftmouse_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


class Target:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('Target.png')
        self.no_bullets_image = load_image('no_bullets.png')
        self.wid, self.hgt = 50, 50
        self.font = load_font('neodgm_code.ttf', 30)
        self.bullet_count = 8
        self.score = 0
        self.loading_time = get_time()
        self.targeting_size = 20

        Target.fire_sound = load_wav('./sound/fire.wav')
        Target.fire_sound.set_volume(32)
        Target.empty_sound = load_wav('./sound/empty.wav')
        Target.empty_sound.set_volume(32)

        if server.game_result == 'FAILED':
            self.targeting_size = 10
            self.wid, self.hgt = 25, 25
        elif server.game_result == 'SUCCESS':
            self.targeting_size = 20
            self.wid, self.hgt = 50, 50

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, 600 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if self.x >= play_mode.player.x - 150 and self.x <= play_mode.player.x + 150:   # shooting range
                self.fire()
                # print(self.x, self.y)
        if event.type == SDL_MOUSEBUTTONUP:
            game_world.remove_collision_object(self)

    def fire(self):
        if self.bullet_count > 0:
            Target.fire_sound.play()
            self.bullet_count -= 1
            bullet = Boom(self.x, self.y)
            game_world.add_object(bullet, 1)
            game_world.add_collision_pair('player:pigeon', self, None)
        else:
            Target.empty_sound.play()


    def update(self):
        # print(server.score)
        if self.bullet_count <= 0:
            server.score += self.score
            if get_time() - self.loading_time >= 2.0:
                game_framework.change_mode(loading_mode)
        pass

    def draw(self):
        if self.bullet_count <= 0:
            self.no_bullets_image.draw(400, 300)
        self.image.draw(self.x, self.y, self.wid, self.hgt)
        self.font.draw(22, 582, f'S{server.stage:.0f} SCORE: {self.score:.0f}', (255, 0, 0))
        self.font.draw(20, 580, f'S{server.stage:.0f} SCORE: {self.score:.0f}', (255, 255, 255))
        self.font.draw(22, 552, f'BULLET: {self.bullet_count:.0f}', (255, 0, 0))
        self.font.draw(20, 550, f'BULLET: {self.bullet_count:.0f}', (255, 255, 255))
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return (self.x - self.targeting_size, self.y - self.targeting_size,
                self.x + self.targeting_size, self.y + self.targeting_size)

    def handle_collision(self, group, other):
        if group == 'player:pigeon':
            # print('collision')
            self.score += 1


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

    def __init__(self, x=400, y=300):
        self.load_images()
        self.frame = 0
        self.x, self.y = x, y

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.frame > 7:
            game_world.remove_object(self)

    def draw(self):
        frame_index = int(self.frame)
        if 0 <= frame_index < len(Boom.images['skill_bullet_1_']):
            Boom.images['skill_bullet_1_'][int(self.frame)].draw(self.x, self.y,
                                                                 200-server.targeting_size, 200-server.targeting_size)
