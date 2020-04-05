import pygame
import json

import GameStates.GameClasses.game_classes as gc
import color as clr

class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

class MenuState(State):
    def __init__(self):
        super().__init__()

        with open('src\config_main.json') as self.config_json_main:
            self.configs_main = json.load(self.config_json_main)

        for config in self.configs_main["main"]:
            self.DISPLAY_WIDTH = config["DISPLAY_WIDTH"]
            self.DISPLAY_HEIGHT = config["DISPLAY_HEIGHT"]

        with open('src\GameStates\GameClasses\config_gc.json') as self.config_json_gc:
            self.configs_gc = json.load(self.config_json_gc)

        for config in self.configs_gc["game_classes"]:
            self.PLAYER_SIDE_LENGTH = config["PLAYER_LENGTH"]

        # TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
        # of just Windows.

        # TODO: Find a way to download/package a font so that this can be done
        # without having to load images and can be blitted normally with text.
        self.one_player_text = pygame.image.load(r'src\GameStates\text_for_1p.jpg')
        self.two_player_text = pygame.image.load(r'src\GameStates\text_for_2p.jpg')
        self.instructions_text = pygame.image.load(r'src\GameStates\text_for_instructions.jpg')

        # Rescale images to better fit the window. Rescaled by a factor of 0.8
        self.one_player_text = pygame.transform.scale(self.one_player_text, (292, 25))
        self.two_player_text = pygame.transform.scale(self.two_player_text, (307, 25))
        self.instructions_text = pygame.transform.scale(self.instructions_text, (474, 24))

        self.all_sprites_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()

        self._load_map()
        self._create_map()

    # I have to create a separate load file as GameMaze.maze is not designed to load start-menu.txt. 
    def _load_map(self):
        # TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
        # of just Windows.
        with open('src\GameStates\start_menu.txt', 'r') as opened_file:
            self.raw_map_file = opened_file.read()

        self.raw_map_file = self.raw_map_file.splitlines()

        self.temp_map_list = []
        self.map_list = []

        for row in self.raw_map_file:
            for character in row:
                self.temp_map_list.append(character)
            
            self.map_list.append(self.temp_map_list)
            self.temp_map_list = []

    def _create_map(self):
        for y_index in range(len(self.map_list)):
            for x_index in range(len(self.map_list[y_index])):
                if self.map_list[y_index][x_index] == "X":
                    self.wall_block = gc.WallBlock(x_index, y_index)
                    
                    self.wall_group.add(self.wall_block)
                    self.all_sprites_group.add(self.wall_block)

    ## Core Function
    def render(self, display):
        display.fill(clr.BLACK)

        self.all_sprites_group.draw(display)

        # TODO: Find a way to use the screen's display width and height to calculate
        # the placement of the text instead of manually changing and adding it.
        # TODO: Center and align text correctly.
        display.blit(self.one_player_text, (80, 320))
        display.blit(self.two_player_text, (400, 320))
        display.blit(self.instructions_text, (160, 400))
    ##

    ## Core Function
    def update(self):
        pass
    ##

    ## Core Function
    def event_handling(self, pressed_buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if pressed_buttons[pygame.K_RETURN]:
                # TODO: Switch the game_state to OnePlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[pygame.K_SPACE]:
                # TODO: Switch the game_state to TwoPlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[pygame.K_i]:
                # TODO: Switch the game_state to InstructionState
                pygame.quit()
                quit()
    #

class OnePlayerGameState(State):
    def __init__(self, player_side_length, display_width, display_height):
        super().__init__()

        self.PLAYER_SIDE_LENGTH = player_side_length
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height

        self.all_sprites_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.player_one = gc.Player(self.PLAYER_SIDE_LENGTH, self.DISPLAY_HEIGHT - 
            (self.PLAYER_SIDE_LENGTH * 2), clr.BLUE)
        self.player_group.add(self.player_one)
        self.all_sprites_group.add(self.player_one)

        self.load_map()
        