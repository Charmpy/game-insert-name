from scripts.level import Level
from scripts.hero import Hero


class MainLoop:
    def __init__(self, counter):
        self.cell_size = 20
        self.board = Level('data/levels/test_lvl')
        self.board.set_view(self.cell_size)
        self.hero = Hero(counter, (5, 5), self.board)
        self.board.add_character(self.hero, (5, 5))

    def render(self, screen):
        self.board.render(screen)

    def action(self, keys):
        self.hero.action(keys)

