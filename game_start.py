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
import time
from game_config import Settings
from game_config import Config
from keybinds import keyboard_commands
from notes import Notes
from audio import Audio
from pygame import mixer
from scoreboard import Scoreboard

class GM:
    def __init__(self):
        pg.init() # Initialize Pygame

        # Initialize Component & Helper Classes
        self.settings = Settings()
        self.config = Config()
        self.screen = pygame.display.set_mode(self.settings.screen_dimensions)
        self.clock = pg.time.Clock()
        self.audio = Audio()
        self.game_powerbox_switch = True
        active_state = ""

    def game_loop(self):
        states = self._game_states()
        key_manager = keyboard_commands(game=self)
        self.scoreboard = Scoreboard(game=self)
        active_state = states.game_start
        st_input = ""  # No Action
        while self.game_powerbox_switch:
            match active_state:
                case states.game_start:
                    st_input = self.pregame_initialization()
                case states.selection:
                    st_input = self.track_selection_screen()
                case states.play:
                    st_input = self.play_track_screen(key_manager)
                case states.results:
                    pass
                case states.credits:
                    pass
                case states.exit:
                    # Cinematic Ending Sequence, ie melodic jingle
                    # Save any possible data necessary
                    pg.quit()
                case _: # equivalent to "else"
                    pass
            # end match
            active_state = states.identify_state_transition(active_state, st_input)
            # Display is in each state
        # end while

    def pregame_initialization(self):
        self.screen.fill("blue")
        self.update_display()
        return

    def track_selection_screen(self):
        # Automatically going to choose Rain Garden
        print("Playing Rain Garden.mp3...")

        # Scoreboard keeps a list of song_data's, use for displaying the tracks on selection screen
        # SONG_NAME = ...
        # self.credits = ...
        # self.settings = ...
        # self.play_song = Button(game=self, text='SONG_NAME')
        # for song in track_list {self.song = Button...}

        '''
        button chosen will reflect the next state, -> Credits || Song || Settings
        - May need to improve infrastructure once multiple songs are added
        '''

        self.update_display()
        # end while
        action = "PLAY"
        return action

    def play_track_screen(self, key_manager):
        notes = Notes(game=self)
        # Draw Tracks + Text

        self.audio.play_music(self.audio.track01)
        while mixer.get_busy() == False:
            # Draw Notes


            for event in pygame.event.get():
                if event.type in key_manager.keyactions:
                    # Peek into respective column (note sprite group) for up/down/etc
                    # Measure distance from track_bottom to closest note (loop through respective sprite group)
                    # - if one sprite group, add value for L R Up D and then if for if col1-U and col2-L, etc
                    pass
            # move notes down
            # update display
        # end while

        action = "RESULTS"
        return action


    def update_display(self):
        pg.display.flip()
        self.clock.tick(self.settings.FPS)
        # delta_time = self.clock.tick(self.settings.FPS) / 1000 for framerate indepdendent physics

    class _game_states:
        def __init__(self):
            self.game_start = "START"
            self.selection = "SELECTION"
            self.play = "PLAY"
            self.results = "RESULTS"
            self.credits = "CREDITS"
            self.exit = "EXIT"
            self.states = [self.game_start, self.selection, self.play, self.results, self.credits, self.exit]

        def identify_state_transition(self, active_state, state_machine_input):
            # Note:
            # States should maintain self state transitions (given an input), may need to alter the structure above
            # ie state NAMES become global and define per-state-transition actions
            next_state = active_state
            if active_state == self.game_start:
                next_state = self.selection
            elif (state_machine_input in self.states):
                next_state = state_machine_input
            return next_state


def main():
    # Initialize an instance of the Game Master (GM) class
    game = GM()
    game.game_loop()

if __name__ == "__main__":
    main()

