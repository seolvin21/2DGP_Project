from pico2d import *
import game_world
import game_framework
import loading_mode
import server


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


# time_out = lambda e : e[0] == 'TIME_OUT'

# character move speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Character Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Idle:

    @staticmethod
    def enter(player, e):
        player.dir = 0
        player.action = 0
        player.frame = 0
        player.wait_time = get_time()
        pass

    @staticmethod
    def exit(player, e):
            pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if get_time() - player.wait_time > 2:
            player.state_machine.handle_event(('TIME_OUT', 0))
    @staticmethod
    def draw(player):
        player.image_idle.clip_draw(int(player.frame) * player.wid, player.action * player.hgt,
                               player.wid, player.hgt, player.x, player.y,
                                    player.wid+70, player.hgt+70)


class Run:

    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            player.dir, player.face_dir, player.action = 1, 1, 0
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            player.dir, player.face_dir, player.action = -1, -1, 0

    @staticmethod
    def exit(player, e):
        if space_down(e):
            pass

    @staticmethod
    def do(player):
        player.x += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        player.x = clamp(25, player.x, 1600 - 25)
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(player):
        if player.dir == -1:
            player.image.clip_draw(int(player.frame) * player.wid, player.action * player.hgt,
                                   player.wid, player.hgt, player.x, player.y,
                                   player.wid+70, player.hgt+70)
        elif player.dir == 1:
            player.image.clip_composite_draw(int(player.frame) * player.wid, player.action * player.hgt,
                                   player.wid, player.hgt, 0, 'h', player.x, player.y,
                                             player.wid+70, player.hgt+70)

class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle: {space_down: Idle, right_down: Run, left_down: Run, left_up: Run, right_up: Run},
            Run: {space_down: Run, right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.player)


class Player:
    def __init__(self):
        self.x, self.y = 400, 30
        self.frame = 0
        self.action = 3
        self.dir = 0
        self.face_dir = 1
        self.wid = 67
        self.hgt = 110
        self.time_limit = 10.0
        self.elapsed_time = 0.0
        self.remaining_time = self.time_limit
        self.image = load_image('player_spritesheet.png')
        self.image_idle = load_image('player_spritesheet_idle.png')
        self.font = load_font('NanumSquareEB.ttf', 30)
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.stage = server.stage

    def update(self):
        self.state_machine.update()
        # Update the timer
        self.elapsed_time += game_framework.frame_time
        self.remaining_time = max(self.time_limit - self.elapsed_time, 0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # Draw the remaining time
        if self.remaining_time > 0:
            self.font.draw(400, 580, f'Remaining Time: {self.remaining_time:.2f}', (255, 255, 255))
            self.font.draw(100, 520, f'STAGE: {self.stage:.0f}', (255, 255, 255))
        else:
            self.font.draw(400, 580, 'Time is up!', (255, 255, 255))
            game_framework.change_mode(loading_mode)