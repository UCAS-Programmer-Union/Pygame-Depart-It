class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

def MenuState(State):
    def __init__(self):
        super().__init__()

    main_menu_main_text = "PYGAME DEPART IT"
    main_menu_subtext = "A clone of Atari 2600 Escape It"
    # TODO: Add buttons to move onto the game instead of having the user type a key.
    main_menu_proceed_instructions_text = "Press ENTER key to start game"

    # TODO: Create a setup.py file to install 8 bit font.
    # As for now, we'll use Arial.
    self.main_font = pygame.font.Sysfont('Arial', 56)
    self.small_font = pygame.font.Sysfont('Arial', 32)