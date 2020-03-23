import pygame
import json

import GameStates.game_states as gs
import color as clr

pygame.init()

# TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
# of just Windows.
with open('src\config_main.json') as config_json:
    configs = json.load(config_json)

for config in configs["main"]:
    FPS = config["FPS"]
    DISPLAY_WIDTH = config["DISPLAY_WIDTH"]
    DISPLAY_HEIGHT = config["DISPLAY_HEIGHT"]

DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    # TODO: Find a way to dynamically pass this in instead of using a magic number.
    # 20 is for the block_side_length
    program_state = gs.MenuState()

    exit = False
    while exit != True:

        pressed_buttons = pygame.key.get_pressed()
        program_state.event_handling(pressed_buttons)

        program_state.update()

        program_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()