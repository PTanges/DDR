'''
Name: Patton Tang
Course: CPSC 386 w Professor McCarthy
Institution: CSU Fullerton

Task: Rhythm Game
- Must include four arrow keys AND simultaneous keypad inputs
- Read further details in game_structure.md
'''

import pygame as pg
import pygame.display
from game_config import Settings
from game_config import Config


class GM:
    def __init__(self):
        pg.init() # Initialize Pygame

        # Initialize Component & Helper Classes
        self.settings = Settings()
        self.config = Config()
        self.screen = pygame.display.set_mode(self.settings.screen_dimensions)
        self.clock = pg.time.Clock()
        self.game_powerbox_switch = True

    def game_loop(self):
        states = self._game_states()
        active_state = states.game_start
        while self.game_powerbox_switch:
            match active_state:
                case states.game_start:
                    pass
                case states.selection:
                    pass
                case states.play:
                    pass
                case states.results:
                    pass
                case states.credits:
                    pass
                case states.exit:
                    pass

    def update_display(self):
        pg.display.flip()
        self.clock.tick(self.settings.FPS)

    class _game_states:
        def __init__(self):
            self.game_start = "START"
            self.selection = "SELECTION"
            self.play = "PLAY"
            self.results = "RESULTS"
            self.credits = "CREDITS"
            self.exit = "EXIT"


def main():
    # Initialize an instance of the Game Master (GM) class
    pass

if __name__ == "__main__":
    main()

