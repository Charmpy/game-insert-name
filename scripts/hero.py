from scripts.character import Character
from scripts.bullet import Bullet


class Hero(Character):
    def __init__(self, counter, pos, level, direction='r'):
        super().__init__(counter, pos, level, direction)

    def __repr__(self):
        return '@'

    def action(self, key):
        if key[119] == 1 and key[97] == 1:
            self.direct = 'ul'
        elif key[119] == 1 and key[100] == 1:
            self.direct = 'ur'
        elif key[115] == 1 and key[100] == 1:
            self.direct = 'dr'
        elif key[115] == 1 and key[97] == 1:
            self.direct = 'dl'
        elif key[119] == 1:
            self.direct = 'u'
        elif key[97] == 1:
            self.direct = 'l'
        elif key[115] == 1:
            self.direct = 'd'
        elif key[100] == 1:
            self.direct = 'r'
        if abs(self.counter.get_bpm() - self.counter.get_couter()) < 10:
            if key[119] == 1 and key[97] == 1:
                self.direct = 'ul'
                self.move()
            elif key[119] == 1 and key[100] == 1:
                self.direct = 'ur'
                self.move()
            elif key[115] == 1 and key[100] == 1:
                self.direct = 'dr'
                self.move()
            elif key[115] == 1 and key[97] == 1:
                self.direct = 'dl'
                self.move()
            elif key[119] == 1:
                self.direct = 'u'
                self.move()
            elif key[97] == 1:
                self.direct = 'l'
                self.move()
            elif key[115] == 1:
                self.direct = 'd'
                self.move()
            elif key[100] == 1:
                self.direct = 'r'
                self.move()
            if key[32] == 1:
                self.fire()

    def fire(self):
        x = self.can_fire()
        if bool(x):
            bullet = Bullet(self.counter, x, self.board, self.direct, 1)
            self.board.add_character(bullet, x)

    def can_fire(self):
        x1, y1 = self.x, self.y

        if self.direct == 'ul':
            rez = self.board.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.':
                x1 -= 1
                y1 -= 1
        elif self.direct == 'ur':
            rez = self.board.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                x1 += 1
                y1 -= 1
        elif self.direct == 'dr':
            rez = self.board.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                x1 += 1
                y1 += 1
        elif self.direct == 'dl':
            rez = self.board.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                x1 -= 1
                y1 += 1
        elif self.direct == 'l':
            rez = self.board.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                x1 -= 1
        elif self.direct == 'u':
            rez = self.board.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                y1 -= 1
        elif self.direct == 'r':
            rez = self.board.get_cell_info(self.x + 1, self.y)
            if rez == '.':
                x1 += 1
        elif self.direct == 'd':
            rez = self.board.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                y1 += 1

        if x1 != self.x or y1 != self.y:
            return (x1, y1)
        return False

