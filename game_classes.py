import pygame
import json

import color as clr

with open("config.json") as config_json:
    configs = json.load(config_json)

for config in configs:
    WALL_BLOCK_WIDTH = configs["WALL_BLOCK_WIDTH"]
    WALL_BLOCK_LENGTH = configs["WALL_BLOCK_LENGTH"]

class Wall_Block(pygame.sprite.Sprite):
    def __init__(self, x_map_index, y_map_index, wall_block_width = WALL_BLOCK_WIDTH,
        wall_block_length = WALL_BLOCK_LENGTH, color = clr.WHITE):
        