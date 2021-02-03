from scripts.level import Level
from scripts.hero import Hero
from random import choice

LEVELS = ['lvl_1', 'lvl_2']


class MainLoop:
    def __init__(self, counter):
        self.counter = counter
        self.cell_size = 20
        self.board = Level('data/levels/test_lvl', self)
        self.board.set_view(self.cell_size)
        self.hero = Hero(self.counter, (1, 7), self.board)
        self.board.add_character(self.hero, (1, 7))

    def render(self, screen):
        self.board.render(screen)

    def get_hero(self):
        return self.hero

    def action(self, keys):
        self.hero.action(keys)

    def change(self):
        pos = choice(self.board.get_spawns())
        self.board = Level(f'data/levels/{choice(LEVELS)}', self)
        self.hero.change_level(self.board)
        self.hero.respawn(pos)
        self.board.set_view(self.cell_size)
        self.board.add_character(self.hero, pos)
        self.hero.change_level(self.board)
