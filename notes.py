import pygame as pg
from pygame.sprite import Sprite
from vector import Vector
from random import randint
from scoreboard import Scoreboard

class Notes:
    note_images = []
    track_arrow_images = []
    track_images = []

    def __init__(self, game):
        self.game = game
        self.initialize_image_files()

        self.screen = game.screen
        self.settings = game.settings
        self.config = game.config
        self.scoreboard = game.scoreboard
        self.gravity = Vector(0, 5)

        self.note_group = pg.sprite.Group()

    def initialize_image_files(self):

        track_arrow_files = []
        NIA = ["Up", "Left", "Right", "Down"]
        self.note_images = [pg.transform.scale(pg.image.load(f'Images/Static/BW_{x}_Arrow.png'), (40, 40)) for
                                   x in NIA]
        self.track_arrow_images = [pg.transform.scale(pg.image.load(f'Images/Static/Frame_{x}_Arrow.png'), (40, 40)) for
                                   x in NIA]
        self.track_images.append(pg.transform.scale(pg.image.load(f'Images/Static/Track_Path.png'), (40,40)))
        self.track_images.append(pg.transform.scale(pg.image.load(f'Images/Static/Track_Bottom.png'), (40,40)))



    def add_note(self, note_column, x, y, note_type):
        note = Note(self.game)
        note.y = y
        note.rect.x, note.rect.y = x, y
        # use note_type to dictate the x and then into the correct note column
        self.note_group.add(note)

    def reset(self):
        self.empty(self.note_group)

    def empty(self, sprite_group):
        sprite_group.empty()

    def randomly_generate_note(self):
        pass

    def check_baseline(self):
        pass
        '''
        for note in self.note_group():
            if note.y > track_bottom.y:
                note.isCrossLine = True
        '''

class Note(Sprite):
    note_images = []
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initialize_image_files()

        self.screen = game.screen
        self.settings = game.settings
        self.config = game.config
        self.scoreboard = game.scoreboard
        self.gravity = Vector(0, 5)

        self.image = self.note_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.isCrossLine = False # ignored by key check once < height of baseline

    def initialize_image_files(self):
        NIA = ["Up", "Left", "Right", "Down"]

        note_image_files = []
        note_image_files.append(f'Images/Static/BW_{x}_Arrow.png' for x in NIA)
        self.note_images = [pg.transform.scale(pg.image.load(x), (40, 40)) for x in note_image_files]

    def update(self, gravity):
        self.y += gravity
        self.rect.y = self.y
        if self.isCrossLine:
            self.kill()
        self.draw()

    def draw(self):
        # self.image = self.timer.current_image() once you want to make a gif of the arrow
        self.screen.blit(self.image, self.rect)

    def check_floor(self):
        # if sprite collides with floor (edge of the screen), kill the sprite
        pass
    '''
    Implementation Idea:
    To assign beats to a beatmap (instead of manual), play the song and map the beats (in real time) to key presses
    - Save to File
    - Read from File
    - Enter a debug menu/action when playing a song
    '''