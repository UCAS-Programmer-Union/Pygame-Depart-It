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

    self.main_text = "PYGAME DEPART IT"
    self.subtext = "A Clone Of Atari 2600 Escape It"
    # TODO: Add buttons to move onto the game instead of having the user type a key.
    self.proceed_instructions = "Press ENTER Key To Start Game"

    # TODO: Create a setup.py file to install 8 bit font.
    # As for now, we'll use Arial.
    self.main_font = pygame.font.Sysfont('Arial', 56)
    self.small_font = pygame.font.Sysfont('Arial', 32)
    
    def render(self, screen):
        screen.fill(clr.BLACK)

        self.rendered_main_text = self.font.render(self.main_text, True, clr.WHITE)
        self.rendered_subtext = self.small_font.render(self.menu_subtext, True, clr.WHITE)
        self.rendered_proceed_instructions = self.small_font.render(self.proceed_instructions, True, clr.WHITE)

        # TODO: Find a way to use the screen's display width and height to calculate
        # the placement of the text instead of manually changing and adding it.
        screen.blit(rendered_menu_main_text, (300, 300))
        screen.blit(rendered_menu_subtext, (300, 360))
        screen.blit(rendered_proceed_instructions, (300, 420))

    def update(self):
        pass

    def event_handling(self, pressed_buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if pressed_buttons[K_SPACE]:
                # TODO: Switch this to the game state.
                pygame.quit()
                quit()