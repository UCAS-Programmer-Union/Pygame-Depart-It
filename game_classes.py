import pygame
import json

import color as clr

with open("config.json") as config_json:
    configs = json.load(config_json)

for config in configs:
    WALL_BLOCK_WIDTH = configs["WALL_BLOCK_WIDTH"]
    WALL_BLOCK_LENGTH = configs["WALL_BLOCK_LENGTH"]

    PLAYER_WIDTH = configs["PLAYER_WIDTH"]
    PLAYER_LENGTH = configs["PLAYER_LENGTH"]
    PLAYER_MOVEMENT_SPEED = configs["PLAYER_MOVEMENT_SPEED"]

class WallBlock(pygame.sprite.Sprite):
    def __init__(self, x_map_index, y_map_index, wall_block_width = WALL_BLOCK_WIDTH,
        wall_block_length = WALL_BLOCK_LENGTH, color = clr.WHITE):
        super().__init__()

        self.width = wall_block_width
        self.length = wall_block_length

        self.image = pygame.Surface([self.width, self.length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x_map_index * self.width
        self.rect.y = y_map_index * self.length

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, player_width = PLAYER_WIDTH, 
        player_length = PLAYER_LENGTH, player_movement = PLAYER_MOVEMENT_SPEED color):
        super().__init__()

        self.player_width = player_width
        self.player_length = player_length

        self.image = self.Surface([self.player_width, self.player_length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = spawn_x
        self.rect.y = spawn_y

        self.movement_speed = player_movement