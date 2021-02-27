from scripts.level import Level
from scripts.hero import Hero
from random import choice

LEVELS = ['lvl_1.txt', 'lvl_2.txt', 'lvl_3.txt', 'lvl_4.txt', 'lvl_5.txt']


class MainLoop:
    def __init__(self, counter, music):
        self.counter = counter
        self.cell_size = 30
        self.board = Level('data/levels/test_lvl.txt', self)
        self.board.set_view(self.cell_size)
        self.hero = Hero(self.counter, (7, 7), self.board)
        self.board.add_character(self.hero, (7, 7))
        self.flag = False
        self.music = music
        self.level_count = 0

    def render(self, screen):
        self.board.render(screen)

    def get_hero(self):
        return self.hero

    def action(self, keys):
        self.hero.action(keys)

    def change(self):
        self.level_count += 1
        pos = choice(self.board.get_spawns())
        if 2 <= self.level_count <= 3:
            lev = LEVELS[1:-2]
        elif 4 <= self.level_count <= 6:
            lev = LEVELS[2:-1]
        elif 6 <= self.level_count:
            lev = LEVELS[2:]
        else:
            lev = [LEVELS[0]]
        self.board = Level(f'data/levels/{choice(lev)}', self)
        self.hero.change_level(self.board)
        self.hero.respawn(pos)
        self.board.set_view(self.cell_size)
        self.board.add_character(self.hero, pos)
        self.hero.change_level(self.board)

    def get_record(self):
        return self.level_count

    def all(self):
        self.flag = True

    def check(self):
        return self.flag
