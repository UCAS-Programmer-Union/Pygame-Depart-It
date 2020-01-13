import pygame
import json

import color as clr

with open("config.json") as config_json:
    configs = json.load(config_json)

for config in configs:
    WALL_BLOCK_WIDTH = configs["WALL_BLOCK_WIDTH"]
    WALL_BLOCK_LENGTH = configs["WALL_BLOCK_LENGTH"]

