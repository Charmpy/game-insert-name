import pygame
import sys
import os
from random import choice


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images',  name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = load_image('floor.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)


WALLS = ['wall1.png', 'wall2.png', 'wall3.png', 'wall4.png', 'wall5.png']


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = load_image(choice(WALLS))
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class Light(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = load_image('fff.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class CharacterSprt(pygame.sprite.Sprite):
    def __init__(self, group, img90, img45):
        super().__init__(group)
        self.original90 = load_image(img90)
        self.original45 = load_image(img45)

        self.image = self.original90
        self.rect = self.image.get_rect().move(-30,  -30)
        self.old = 'u'

    def update(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x,  pos_y

    def rotate(self, direct):
        if direct == 'ul':
            self.image = pygame.transform.rotate(self.original45, 90)
        elif direct == 'ur':
            self.image = pygame.transform.rotate(self.original45, 0)
        elif direct == 'dr':
            self.image = pygame.transform.rotate(self.original45, -90)
        elif direct == 'dl':
            self.image = pygame.transform.rotate(self.original45, 180)
        elif direct == 'l':
            self.image = pygame.transform.rotate(self.original90, 90)
        elif direct == 'u':
            self.image = pygame.transform.rotate(self.original90, 0)
        elif direct == 'r':
            self.image = pygame.transform.rotate(self.original90, -90)
        elif direct == 'd':
            self.image = pygame.transform.rotate(self.original90, 180)


class BulletSprt(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = load_image('fireball.png')
        self.rect = self.image.get_rect().move(-30,  -30)

    def update(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x,  pos_y


class DoorSprt(pygame.sprite.Sprite):
    def __init__(self, group, mode):
        super().__init__(group)
        self.image_open = load_image('floor.png')
        self.image_close = load_image('wall1.png')
        self.mode = mode
        if self.mode:
            self.image = self.image_open
        else:
            self.image = self.image_open
        self.rect = self.image.get_rect().move(-30,  -30)

    def set_mode(self, rez):
        self.mode = rez

    def update(self, pos_x, pos_y):
        if self.mode:
            self.image = self.image_open
        else:
            self.image = self.image_close
        self.rect = self.image.get_rect().move(pos_x, pos_y)
