import os
import discord
from zaycev import Zaycev

class Player():

    def __init__(self, voice):
         self.voice = voice

    
    def play_list(self, path_list):
        number = 0
        if self.voice.is_done():
            number += 1
            self.voice.play(discord.FFmpegPCMAudio(path_list[number]))
        else:
            self.voice.play(discord.FFmpegPCMAudio(path_list[number]))


    def play_track(self, path):
        self.voice.play(discord.FFmpegPCMAudio(path), after=None)

    def pause(self):
        self.voice.pause()

    def unpause(self):
        self.voice.resume()

    def stop(self):
        self.voice.stop()
