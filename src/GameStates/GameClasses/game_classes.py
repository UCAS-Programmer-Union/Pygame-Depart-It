import pygame
import json

import color as clr

# TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
# of just Windows.
with open('src\GameStates\GameClasses\config_gc.json') as config_json:
    configs = json.load(config_json)

for config in configs["game_classes"]:
    WALL_BLOCK_WIDTH = config["WALL_BLOCK_WIDTH"]
    WALL_BLOCK_LENGTH = config["WALL_BLOCK_LENGTH"]

    PLAYER_WIDTH = config["PLAYER_WIDTH"]
    PLAYER_LENGTH = config["PLAYER_LENGTH"]
    PLAYER_MOVEMENT_SPEED = config["PLAYER_MOVEMENT_SPEED"]

class WallBlock(pygame.sprite.Sprite):
    def __init__(self, x_map_index, y_map_index, color = clr.WHITE, 
        wall_block_width = WALL_BLOCK_WIDTH, wall_block_length = WALL_BLOCK_LENGTH):
        super().__init__()

        self.width = wall_block_width
        self.length = wall_block_length

        self.image = pygame.Surface([self.width, self.length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x_map_index * self.width
        self.rect.y = y_map_index * self.length

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, color, player_width = PLAYER_WIDTH, 
        player_length = PLAYER_LENGTH, player_movement = PLAYER_MOVEMENT_SPEED):
        super().__init__()

        self.player_width = player_width
        self.player_length = player_length

        self.image = self.Surface([self.player_width, self.player_length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = spawn_x
        self.rect.y = spawn_y

        self.movement_speed = player_movement

    def movement(self, direction):
        if direction == "left":
            self.rect.x -= direction
        elif direction == "right":
            self.rect.x += direction
        elif direction == "up":
            self.rect.y -= direction
        elif direction == "down":
            self.rect.y += direction

    # This is checking if the player has gone off the top or bottom walls.
    # Kinda backwards that the x-axis checks the rect.y. Oh well.
    def x_axis_boundary_check(self):
        # TODO: Change this so that it stops the user before they go off screen to
        # avoid them slingshotting back into the screen.
        if self.rect.y < 0:
            self.rect.y = 0
        # TODO: Change this so that the 600 is replaced by a variable or argument of some sort
        # so that you don't have to come back and change this every time you change
        # the screen resolution.
        elif (self.rect.y + self.player_width) > 480: # 800 is the screen's height.
            self.rect.y = 480 - self.player_width

    # This is checking if the player has gone off the left or right walls.
    # Once again, this is kinda backwards that the y-axis checks the rect.x. Oh well.
    def y_axis_boundary_check(self):
        # TODO: Change this so that it stops the user before they go off screen to
        # avoid them slingshotting back into the screen.
        if self.rect.x < 0:
            self.rect.x = 0
        # TODO: Change this so that the 600 is replaced by a variable or argument of some sort
        # so that you don't have to come back and change this every time you change
        # the screen resolution.
        elif (self.rect.x + self.player_length) > 800: # 800 is the screen's width.
            self.rect.x = 800 - self.player_length

    def update(self):
        self.x_axis_boundary_check()
        self.y_axis_boundary_check()
        