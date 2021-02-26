import pygame


class Music:
    def __init__(self, counter):
        self.counter = counter
        self.delay = 0
        self.step = pygame.mixer.Sound('data/music/step.ogg')
        self.fire = pygame.mixer.Sound('data/music/fire.ogg')
        self.beat = pygame.mixer.Sound('data/music/theme.ogg')

    def start(self):
        pygame.mixer.music.load('data/music/back.ogg')
        pygame.mixer.music.play(-1)

    def play(self):
        if self.counter.get_counter() == 30 \
                and self.delay == 0:
            pygame.mixer.Sound.play(self.beat)
            self.delay = 1
        elif self.counter.get_counter() == 30 \
                and self.delay == 1:
            self.delay = 0

    def play_step(self):
        pygame.mixer.Sound.play(self.step)

    def play_fire(self):
        pygame.mixer.Sound.play(self.fire)
