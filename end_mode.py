from pico2d import *
import game_framework
import loading_mode
import server
import start_mode

def init():
    global image
    global font

    image = load_image('./background/BG_1_1.png')
    server.ranking.append(server.score)

    font = load_font('neodgm_code.ttf', 40)
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    # 서버의 랭킹을 score에 따라 정렬
    sorted_ranking = sorted(server.ranking, reverse=True)

    # 랭킹 출력
    for i, score in enumerate(sorted_ranking):
        font.draw(270, 300 - i * 50, f'RANK {i + 1}: {score}', (255, 255, 255))

    font.draw(50, 100, f'NEW GAME: SPACE', (255, 255, 255))
    font.draw(50, 60, f'QUIT: ESC', (255, 255, 255))
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
