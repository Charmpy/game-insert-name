from scripts.character import Character
from scripts.graphics import BulletSprt


class Bullet(Character):
    def __init__(self, counter, pos, level, direction, speed):
        super().__init__(counter, pos, level, direction)
        self.speed = speed
        self.kill_info = False
        self.sprite = BulletSprt(pos[0], pos[1], level.all_sprites)

    def __repr__(self):
        return 'B'

    def draw(self, x, y):
        self.sprite.update(x, y)

    def move(self):
        x1, y1 = self.x, self.y

        if self.direct == 'ul':
            rez = self.level.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.' or str(rez) == 'E':
                self.x -= 1
                self.y -= 1
            if str(rez) == 'E':
                self.x -= 1
                self.y -= 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'ur':
            rez = self.level.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                self.x += 1
                self.y -= 1
            elif str(rez) == 'E':
                self.x += 1
                self.y -= 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'dr':
            rez = self.level.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                self.x += 1
                self.y += 1
            elif str(rez) == 'E':
                self.x += 1
                self.y += 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'dl':
            rez = self.level.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                self.x -= 1
                self.y += 1
            elif str(rez) == 'E':
                self.x -= 1
                self.y += 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'l':
            rez = self.level.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                self.x -= 1
            elif str(rez) == 'E':
                self.x -= 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'u':
            rez = self.level.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                self.y -= 1
            elif str(rez) == 'E':
                self.y -= 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'r':
            rez = self.level.get_cell_info(self.x + 1, self.y)
            if rez == '.':
                self.x += 1
            elif str(rez) == 'E':
                self.x += 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        elif self.direct == 'd':
            rez = self.level.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                self.y += 1
            elif str(rez) == 'E':
                self.y += 1
                self.level.move_sprites.remove(rez.get_sprite())
                self.level.clear_cell((self.x, self.y))
                self.level.move_object((x1, y1), (self.x, self.y))
                self.kill_info = True
            elif rez == '#' or str(rez) == 'D' or rez == 'F':
                self.kill_info = True
        if not self.kill_info:
            self.level.move_object((x1, y1), (self.x, self.y))
        else:
            self.level.clear_cell((self.x, self.y))

            # self.sprite.update(-30, -30)
            self.level.all_sprites.remove(self.sprite)

    def set_move(self):
        if (
            self.counter.get_bpm() // self.speed == self.counter.get_counter()
            and self.counter.get_bpm() % self.speed == 0
        ):
            self.move()
