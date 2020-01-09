import pygame
import json

import color as clr

pygame.init()

with open('config.json') as config_json:
    configs = json.load(config_json)

for config in configs["main"]:
    FPS = config["FPS"]
    DISPLAY_WIDTH = config["DISPLAY_WIDTH"]
    DISPLAY_HEIGHT = config["DISPLAY_HEIGHT"]

DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    