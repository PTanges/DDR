import pygame as pg

class keyboard_commands:
    def __init__(self, game):
        self.game = game
        self.initialize_default_keybinds()

    def initialize_default_keybinds(self):
        self.up = pg.K_UP
        self.left = pg.K_LEFT
        self.right = pg.K_RIGHT
        self.down = pg.K_DOWN

    def filter_valid_keypresses(self):
        keys = pg.key.get_pressed()
        actions = []
        if keys[self.up]: actions.append("UP")
        if keys[self.left]: actions.append("LEFT")
        if keys[self.right]: actions.append("RIGHT")
        if keys[self.down]: actions.append("DOWN")
        return actions

    # Accessibility to do: Implement alternative keybinds through a Settings screen accessible on the Track Screen
    def set_keybind(self):
        # Take user input (from keyboard OR external tools, ie mouse or controller)
        # Validate -> Map to internal value
        pass

    def set_keybinds(self):
        # match case from button, [1-3] for the dev defined keybinds
        # Keybinds: ASDF, WASD, QWER, and user-defined
        pass