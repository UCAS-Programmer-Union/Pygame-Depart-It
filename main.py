import pygame
import json

import color as clr

pygame.init()

with open('config.json') as config_json:
    configs = json.load(config_json)