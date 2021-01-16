import pygame


class Character:
    def __init__(self, counter, pos, level, direction='r'):
        self.x, self.y = pos
        self.board = level
        self.direct = direction
        self.counter = counter

    def set_direction(self, direction):
        self.direct = direction

    def __repr__(self):
        return 'C'

    def move(self):
        x1, y1 = self.x, self.y

        if self.direct == 'ul':
            rez = self.board.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.':
                self.x -= 1
                self.y -= 1
        elif self.direct == 'ur':
            rez = self.board.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                self.x += 1
                self.y -= 1
        elif self.direct == 'dr':
            rez = self.board.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                self.x += 1
                self.y += 1
        elif self.direct == 'dl':
            rez = self.board.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                self.x -= 1
                self.y += 1
        elif self.direct == 'l':
            rez = self.board.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                self.x -= 1
        elif self.direct == 'u':
            rez = self.board.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                self.y -= 1
        elif self.direct == 'r':
            rez = self.board.get_cell_info(self.x + 1, self.y)
            if rez == '.':
                self.x += 1

        elif self.direct == 'd':
            rez = self.board.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                self.y += 1
        self.board.move_character((x1, y1), (self.x, self.y))
