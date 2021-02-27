from scripts.level import Level
from scripts.hero import Hero
from random import choice

LEVELS = ['lvl_1', 'lvl_2', 'lvl_3', 'lvl_4', 'lvl_5']


class MainLoop:
    def __init__(self, counter, music):
        self.counter = counter
        self.cell_size = 30
        self.board = Level('data/levels/test_lvl', self)
        self.board.set_view(self.cell_size)
        self.hero = Hero(self.counter, (1, 7), self.board)
        self.board.add_character(self.hero, (1, 7))
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


