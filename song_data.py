import pygame as pg

class Song_Data:
    difficulties = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self):
        self._song_name = ""
        self._song_difficulty = ""
        self._longest_streak = 0
        self._total_notes = 0
        self.note_accuracy_scoreboard = {"Miss": 0, "Good": 0, "Great": 0, "Perfect": 0}
        self._isCleared = False

    def set_song_completion(self):
        self._isCleared = True

    @property
    def song_completion_status(self):
        return self._isCleared

    @property
    def total_notes(self):
        return self._total_notes

    @property
    def song_name(self):
        return self._song_name

    @property
    def longest_streak(self):
        return self._longest_streak

    @property
    def song_difficulty(self):
        return self._song_difficulty

    def export_song_data(self):
        # write save data above to a file
        pass

    def import_song_data(self):
        # with open file read for file_name in glob.walk of the Tracks folder,
        # read the sav files with matching names (truncate.mp3)
        pass