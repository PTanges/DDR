import pygame as pg
from pygame import mixer
import time

'''
Documentation:
Link - < https: // www.pygame.org / docs / ref / music.html >
'''


class Audio:
    _URL_PREFIX = "Sounds/Tracks/"
    track01 = _URL_PREFIX + "Rain Garden.mp3"
    default_volume = 0.5
    # glob walk tracks file for all track names

    def __init__(self):
        mixer.init()
        self.volume = self.default_volume
        self.set_volume(self.volume)
        # self.sfx_library = {"KEY": mixer.sound("filepath")}
        # filepath would be Sounds/SFX/... .mp3 or .wav

    def set_volume(self, volume):
        mixer.music.set_volume(volume)

    def play_music(self, filename):
        mixer.music.stop()
        mixer.music.load(self.track01)
        mixer.music.play(loops=-1)

    def pause_music(self):
        mixer.music.pause()

    def unpause_music(self):
        mixer.music.unpause()

    def stop_music(self):
        mixer.music.stop()
        mixer.music.unload()