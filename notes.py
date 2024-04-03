import pygame as pg
from pygame.sprite import Sprite
from vector import Vector
from random import randint
from scoreboard import Scoreboard
from keybinds import keyboard_commands

class Notes:
    note_images = []
    track_arrow_images = []
    track_images = []

    def __init__(self, game):
        self.game = game
        self.initialize_image_files()

        self.screen: pg.Surface = game.screen # encforcement
        self.settings = game.settings
        self.config = game.config
        self.scoreboard = game.scoreboard
        self.gravity = Vector(0, 5)

        '''
        self.current_combo_score = 0
        self.combo_high_score = 0
        self.isComboing = False
        # May not be in this class, in update for note where kill for set combo = False
        '''

        self.note_group = pg.sprite.Group()


    def initialize_image_files(self):
        track_arrow_files = []
        NIA = ["Up", "Left", "Right", "Down"]
        self.note_images = [pg.transform.scale(
            pg.image.load(f'Images/Static/BW_{x}_Arrow.png'), (40, 40)) for x in NIA]
        self.track_arrow_images = [pg.transform.scale(
            pg.image.load(f'Images/Static/Frame_{x}_Arrow.png'), (40, 40)) for x in NIA]
        # enforce the -8 syntax rules (char limit per line)

    ''' # referenced from Aliens in Galga
    def add_note(self, note_column, x, y, note_type):
        note = Note(self.game)
        note.y = y
        note.rect.x, note.rect.y = x, y
        # use note_type to dictate the x and then into the correct note column
        self.note_group.add(note)
    '''

    def reset(self):
        self.empty(self.note_group)

    def empty(self, sprite_group):
        sprite_group.empty()

    def randomly_generate_note(self):
        note = Note(self.game)
        position = randint(1, 4) # [1,4] inclusive
        note.direction = note.note_types[position-1]
        note.y = 0
        note.x = (position * 2) - 1
        note.image = self.note_images[position - 1]
        note.rect.x = note.x * (self.screen.get_width() // 9) + (40 / 2)
        note.rect.y = note.y
        self.note_group.add(note)

    def compare_keypress_with_notes(self, event_type, key_manager):
        if len(self.note_group) > 0:
            _note = self.find_nearest_arrow(event_type, key_manager)
            if _note == None: return

            distance = self.measure_note_distance()
            _grace_distance = self.settings.note_leniency
            if distance < _grace_distance and distance >= 0: _note.delete_note() # Perfect
            elif distance < (_grace_distance * 2) and distance >= _grace_distance: _note.delete_note() # Great
            elif distance < (_grace_distance * 3) and distance >= (_grace_distance * 2): _note.delete_note() # Good
            elif distance < (_grace_distance * 5) and distance >= (_grace_distance * 3): _note.delete_note() # Miss
            else: return # outside of range, no action taken
        # end funct

    def find_nearest_arrow(self, event_type, key_manager):
        note = Note(self.game)
        _keypress_direction = key_manager.translate_default_key_event(event_type)
        _track_notes = []

        # Parse notes in the same column as keypress_direction
        for _note in self.note_group:
            if _note.direction == _keypress_direction:
                _track_notes.append(_note)

        note = _track_notes[0]

        return note

    def measure_note_distance(self, note):
        # Assign accuracy as well
        # distance = (note.rect.y - track bottom), will need a funct for track bottom
        distance = self.settings.screen_height - 240 - note.y
        # where 560 is the height of the track WITHOUT the bottom

        # Current Implementation: Index[0] of the spritegroup on a specific track
        # will be considered "on"/collision with the track bottom at all times
        # since there's grace, we do NOT want to use spritegroup.collision
        # distance = 0
        return distance

    ''' # redundant, in note sprite
    def check_baseline(self):
        pass
        
        for note in self.note_group():
            if note.y > track_bottom.y:
                note.isCrossLine = True
    '''

class Note(Sprite):
    note_images = []
    note_types = ["UP", "LEFT", "RIGHT", "DOWN"]
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initialize_image_files()

        self.screen = game.screen
        self.settings = game.settings
        self.config = game.config
        self.scoreboard = game.scoreboard
        self.gravity = Vector(0, 2.5)
        self._direction = ""

        self.image = self.note_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.isCrossLine = False # ignored by key check once < height of baseline

    def initialize_image_files(self):
        NIA = ["Up", "Left", "Right", "Down"]

        note_image_files = [f'Images/Static/BW_{x}_Arrow.png' for x in NIA]
        self.note_images = [pg.transform.scale(pg.image.load(file),(40, 40))
                            for file in note_image_files]

    def update(self):
        self.y += self.gravity.y
        self.rect.y = self.y
        self.check_floor()
        if self.isCrossLine:
            print(f'{self.direction} arrow terminated!')
            self.kill()

    def draw(self):
        # self.image = self.timer.current_image() once you want to make a gif of the arrow
        self.screen.blit(self.image, self.rect)

    def check_floor(self):
        if self.rect.y > self.screen.get_height():
            self.isCrossLine = True

    def delete_note(self):
        # Score Information here perhaps
        self.kill()

    property
    def direction(self):
        return self._direction
    '''
    Implementation Idea:
    To assign beats to a beatmap (instead of manual), play the song and map the beats (in real time) to key presses
    - Save to File
    - Read from File
    - Enter a debug menu/action when playing a song
    '''

class Track(Sprite):
    def __init__(self, size, x, y, isBottom):
        super().__init__()
        self.image: pg.Surface

        if isBottom:
            self.image = pg.transform.scale(
                pg.image.load(f'../../Downloads/DDR/DDR/Images/Static/Track_Bottom.png'),
                (size, size))
        else:
            self.image = pg.transform.scale(
                pg.image.load(f'../../Downloads/DDR/DDR/Images/Static/Track_Path.png'),
                (size, size))
        
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x