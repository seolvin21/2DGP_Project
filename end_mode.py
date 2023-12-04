from pico2d import *
import game_framework
import loading_mode
import server
import start_mode

def init():
    global image
    image = load_image('./background/BG_1_1.png')
    server.ranking.append(server.score)
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(start_mode)
    pass
