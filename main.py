from pico2d import *
import loading_mode

open_canvas()

loading_mode.init()
# game loop
while loading_mode.running:
    loading_mode.handle_events()
    loading_mode.update()
    loading_mode.draw()
    delay(0.01)

loading_mode.finish()
close_canvas()
