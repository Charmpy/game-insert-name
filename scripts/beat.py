import pygame


class Beat:
    def __init__(self, bpm, counter):
        self.counter = counter
        self.bpm = bpm
        self.x, self.y = 100, 50
        self.left, self.top = 10, 10
        self.k = 0

    def set_geometry(self, size, pos):
        self.x, self.y = size
        self.left, self.top = pos

    def render(self, screen):
        pygame.draw.rect(
            screen, pygame.Color('pink'),
            (
                self.left, self.top, self.x, self.y
            ), 5
        )
        pygame.draw.rect(
            screen, pygame.Color('white'),
            (
                self.left + self.x // 2 - 10, self.top, 20, self.y
            ), 3
        )
        counter = self.counter.get_couter()
        pygame.draw.line(
            screen, pygame.Color('blue'),
            (self.left + 25 + (self.x // 2 // self.bpm) * counter, self.top),
            (self.left + 25 + (self.x // 2 // self.bpm) * counter, self.top + self.y), 3
        )
        pygame.draw.line(
            screen, pygame.Color('blue'),
            (self.left + self.x - (self.x // 2 // self.bpm) * counter - 25, self.top),
            (self.left + self.x - (self.x // 2 // self.bpm) * counter - 25,
             self.top + self.y), 3
        )



