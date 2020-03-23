import pygame

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

    # TODO: Find a way to download/package a font so that this can be done
    # without having to load images and can be blitted normally with text.
    self.one_player_text = pygame.image.load('text_for_1p.jpg')
    self.two_player_text = pygame.image.load('text_for_2.jpg')
    self.instructions_text = pygame.image.load('text_for_instructions')

    # I have to create a separate load file as GameMaze.maze is not designed to load start-menu.txt. 
    def _load_map(self):
        with open('start_menu.txt', 'r') as opened_file:
            self.raw_map_file = opened_file.read()

        self.raw_map_file = self.raw_map_file.splitlines()

        self.temp_map_list = []
        self.map_list = []

        for row in self.raw_map_file:
            for character in row:
                self.temp_map_list.append(character)
            
            self.map_list.appened(self.temp_map_list)
            self.temp_map_list = []

    ## Core Function
    def render(self, screen):
        screen.fill(clr.BLACK)

        # TODO: Find a way to use the screen's display width and height to calculate
        # the placement of the text instead of manually changing and adding it.
        # TODO: Center and align text correctly.
        screen.blit(self.one_player_text, (80, 340))
        screen.blit(self.two_player_text, (400, 340))
        screen.blit(self.instructions_text, (160, 420))
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

            if pressed_buttons[K_RETURN]:
                # TODO: Switch the game_state to OnePlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[K_SPACE]:
                # TODO: Switch the game_state to TwoPlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[KEY_i]:
                # TODO: Switch the game_state to InstructionState
                pygame.quit()
                quit()
    ##