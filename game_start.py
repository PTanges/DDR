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
from notes import Note as Note_Class
from notes import Track
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
        self.background = self.screen.copy()
        self.clock = pg.time.Clock()
        self.audio = Audio()
        self.game_powerbox_switch = True
        self.sprites = pg.sprite.Group()
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
        # Move to Play once mult tracks are added
        self.create_tracks()
        self.screen.fill("black")
        self.update_display()
        return

    def track_selection_screen(self):
        # Automatically going to choose Rain Garden
        print("Playing Rain Garden.mp3...")

        # Scoreboard keeps a list of song_data's,
        # use for displaying the tracks on selection screen
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
        self.audio.play_music(self.audio.track01)
        notes.randomly_generate_note()
        ticks = 0
        prev_ticks = 0
        while mixer.get_busy() == False:
            if ticks < prev_ticks:
                notes.randomly_generate_note()
            prev_ticks = ticks

            for event in pygame.event.get():
                if event.type in key_manager.keyactions:
                    # Play a 'donk' sfx (SFX by Toby Fox would be appropriate)
                    # with a rand.pitch +/-0.05, with "Perfect" being the highest...

                    # Peek into respective column (note sprite group) for up/down/etc
                    # Measure distance from track_bottom to closest note
                    # (loop through respective sprite group)
                    # - if one sprite group, add value for L R Up D
                    # and then if for if col1-U and col2-L, etc
                    pass
                elif event.type == pg.QUIT:
                    action = "EXIT"
                    return action
            # move notes down
            notes.note_group.update()

            self.screen.fill("black") # fill required each time or once?
            self.sprites.add(notes.note_group)
            self.sprites.draw(self.screen)
            self.update_display()
            
            delta = self.clock.tick(self.settings.FPS)
            ticks = (ticks + delta) % 500
        # end while

        action = "RESULTS"
        return action


    def update_display(self):
        pg.display.update()

    def create_tracks(self):
        track_size = 40
        track_x_distance = self.screen.get_width() // 9
        track_length = self.screen.get_width() // track_size

        x = 1
        for _ in range(4):
            track_y = self.screen.get_height() - track_size
            track_x = (track_x_distance * x) + (track_size / 2)
            self.sprites.add(Track(
                size=track_size,
                x=track_x,
                y=track_y,
                isBottom=True))
            x += 2
        
        section: pg.Surface
        x = 1
        y = 1 # Count including the track bottom
        for _ in range(4):
            for _ in range(track_length):
                track_y = self.screen.get_height() - (track_size * y)
                track_x = (track_x_distance * x) + (track_size / 2)
                self.sprites.add(Track(
                    size=track_size,
                    x=track_x,
                    y=track_y,
                    isBottom=False))
                y += 1
            x += 2
            y = 1
    
    class _game_states:
        def __init__(self):
            self.game_start = "START"
            self.selection = "SELECTION"
            self.play = "PLAY"
            self.results = "RESULTS"
            self.credits = "CREDITS"
            self.exit = "EXIT"
            self.states = [self.game_start, self.selection, self.play,
                            self.results, self.credits, self.exit]

        def identify_state_transition(self, active_state, state_machine_input):
            # Note:
            # States should maintain self state transitions (given an input),
            # may need to alter the structure above
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

