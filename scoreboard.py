import pygame as pg
from song_data import Song_Data

class Scoreboard:
    def __init__(self, game):
        self.scores = {}
        self.song_list = [] # track names in order
        '''
        for (song in tracks) and matches save.file data
            self.scores["Song_Name"] = Song_Data object
        '''

    def get_song_difficulty(self, song_name):
        return self.scores[song_name].song_difficulty

    def get_song_streak(self, song_name):
        return self.scores[song_name].longest_streak

    def get_total_notes(self, song_name):
        return self.scores[song_name].total_notes