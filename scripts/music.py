import pygame


class Music:
    def __init__(self, counter):
        self.counter = counter

    def play(self):
        pygame.mixer.music.load('data/music/theme.ogg')
        pygame.mixer.music.play(-1)
