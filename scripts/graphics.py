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


class HeroSprt(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('gg90.png')
        self.rect = self.image.get_rect().move(-30,  -30)

    def update(self, pos_x, pos_y, direct):
        pic = self.image.copy()
        print(direct)
        if direct == 'ul':
            pass
        elif direct == 'ur':
            pass
        elif direct == 'dr':
            pass
        elif direct == 'dl':
            pass
        elif direct == 'l':
            pic = pygame.transform.rotate(pic, 90)
        elif direct == 'u':
            pic = pygame.transform.rotate(pic, 0)
        elif direct == 'r':
            pic = pygame.transform.rotate(pic, -90)
        elif direct == 'd':
            pic = pygame.transform.rotate(pic, 180)
        self.rect = pic.get_rect()
        self.rect.x, self.rect.y = pos_x,  pos_y


class BulletSprt(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = load_image('fireball.png')
        self.rect = self.image.get_rect().move(-30,  -30)

    def update(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x,  pos_y
