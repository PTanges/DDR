import pygame as pg
from song_data import Song_Data

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.scores = {}
        self.song_list = [] # track names in order

        self.current_track_name = ""
        '''
        for (song in tracks) and matches save.file data
            self.scores["Song_Name"] = Song_Data object
        '''

    def get_current_song_difficulty(self):
        return self.scores[self.current_track_name].song_difficulty

    def get_current_song_longest_streak(self):
        return self.scores[self.current_track_name].longest_streak

    def get_current_song_total_notes(self):
        return self.scores[self.current_track_name].total_notes

    def increment_score(self):
        pass

    # Note: Should streak be here instead of in notes?

    def get_song_difficulty(self, song_name):
        return self.scores[song_name].song_difficulty

    def get_song_longest_streak(self, song_name):
        return self.scores[song_name].longest_streak

    def get_total_notes(self, song_name):
        return self.scores[song_name].total_notes