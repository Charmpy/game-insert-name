from scripts.character import Character


class Bullet(Character):
    def __init__(self, counter, pos, level, direction, speed):
        super().__init__(counter, pos, level, direction)
        self.speed = speed
        self.kill_info = False

    def __repr__(self):
        return 'B'

    def move(self):
        x1, y1 = self.x, self.y

        if self.direct == 'ul':
            rez = self.board.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.' or str(rez) == 'E':
                self.x -= 1
                self.y -= 1
            if str(rez) == 'E':
                self.x -= 1
                self.y -= 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'ur':
            rez = self.board.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                self.x += 1
                self.y -= 1
            elif str(rez) == 'E':
                self.x += 1
                self.y -= 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'dr':
            rez = self.board.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                self.x += 1
                self.y += 1
            elif str(rez) == 'E':
                self.x += 1
                self.y += 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'dl':
            rez = self.board.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                self.x -= 1
                self.y += 1
            elif str(rez) == 'E':
                self.x -= 1
                self.y += 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'l':
            rez = self.board.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                self.x -= 1
            elif str(rez) == 'E':
                self.x -= 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'u':
            rez = self.board.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                self.y -= 1
            elif str(rez) == 'E':
                self.y -= 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'r':
            rez = self.board.get_cell_info(self.x + 1, self.y)
            # for i in self.board._get_structure():
            #     print(i)
            if rez == '.':
                self.x += 1
            elif str(rez) == 'E':
                self.x += 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        elif self.direct == 'd':
            rez = self.board.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                self.y += 1
            elif str(rez) == 'E':
                self.y += 1
                self.board.clear_cell((self.x, self.y))
            elif rez == '#':
                self.kill_info = True
        if not self.kill_info:
            self.board.move_object((x1, y1), (self.x, self.y))
        else:
            self.board.clear_cell((self.x, self.y))

    def set_move(self):
        if (
            self.counter.get_bpm() // self.speed == self.counter.get_couter()
            and self.counter.get_bpm() % self.speed == 0
        ):
            self.move()
