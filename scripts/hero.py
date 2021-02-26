from scripts.character import Character
from scripts.bullet import Bullet
from scripts.graphics import HeroSprt


class Hero(Character):
    def __init__(self, counter, pos, level, direction='r'):
        super().__init__(counter, pos, level, direction)
        self.sprite = HeroSprt(level.all_sprites)

    def __repr__(self):
        return '@'

    def draw(self, x, y):
        self.sprite.update(x, y, self.direct)

    def respawn(self, pos):
        self.x, self.y = pos

    def change_level(self, level):
        self.level = level

    def action(self, key):
        if abs(self.counter.get_bpm() - self.counter.get_counter()) < 10:
            if key[119] == 1 and key[97] == 1:
                self.direct = 'ul'
                self.move()
                self.level.loop.music.play_step()
            elif key[119] == 1 and key[100] == 1:
                self.direct = 'ur'
                self.move()
                self.level.loop.music.play_step()
            elif key[115] == 1 and key[100] == 1:
                self.direct = 'dr'
                self.move()
                self.level.loop.music.play_step()
            elif key[115] == 1 and key[97] == 1:
                self.direct = 'dl'
                self.move()
                self.level.loop.music.play_step()
            elif key[119] == 1:
                self.direct = 'u'
                self.move()
                self.level.loop.music.play_step()
            elif key[97] == 1:
                self.direct = 'l'
                self.move()
                self.level.loop.music.play_step()
            elif key[115] == 1:
                self.direct = 'd'
                self.move()
                self.level.loop.music.play_step()
            elif key[100] == 1:
                self.direct = 'r'
                self.move()
                self.level.loop.music.play_step()
            if key[32] == 1:
                self.fire()
        else:
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

    def move(self):
        x1, y1 = self.x, self.y
        if self.direct == 'ul':
            rez = self.level.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.':
                self.x -= 1
                self.y -= 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'ur':
            rez = self.level.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                self.x += 1
                self.y -= 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'dr':
            rez = self.level.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                self.x += 1
                self.y += 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'dl':
            rez = self.level.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                self.x -= 1
                self.y += 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'l':
            rez = self.level.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                self.x -= 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'u':
            rez = self.level.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                self.y -= 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'r':
            rez = self.level.get_cell_info(self.x + 1, self.y)
            if rez == '.':
                self.x += 1
            if str(rez) == 'D':
                rez.teleport()

        elif self.direct == 'd':
            rez = self.level.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                self.y += 1
            if str(rez) == 'D':
                rez.teleport()

        self.level.move_object((x1, y1), (self.x, self.y))

    def fire(self):
        x = self.can_fire()
        if bool(x):
            bullet = Bullet(self.counter, x, self.level, self.direct, 1)
            self.level.add_character(bullet, x)
            self.level.loop.music.play_fire()

    def can_fire(self):
        x1, y1 = self.x, self.y
        if self.direct == 'ul':
            rez = self.level.get_cell_info(self.x - 1, self.y - 1)
            if rez == '.':
                x1 -= 1
                y1 -= 1
        elif self.direct == 'ur':
            rez = self.level.get_cell_info(self.x + 1, self.y - 1)
            if rez == '.':
                x1 += 1
                y1 -= 1
        elif self.direct == 'dr':
            rez = self.level.get_cell_info(self.x + 1, self.y + 1)
            if rez == '.':
                x1 += 1
                y1 += 1
        elif self.direct == 'dl':
            rez = self.level.get_cell_info(self.x - 1, self.y + 1)
            if rez == '.':
                x1 -= 1
                y1 += 1
        elif self.direct == 'l':
            rez = self.level.get_cell_info(self.x - 1, self.y)
            if rez == '.':
                x1 -= 1
        elif self.direct == 'u':
            rez = self.level.get_cell_info(self.x, self.y - 1)
            if rez == '.':
                y1 -= 1
        elif self.direct == 'r':
            rez = self.level.get_cell_info(self.x + 1, self.y)
            if rez == '.':
                x1 += 1
        elif self.direct == 'd':
            rez = self.level.get_cell_info(self.x, self.y + 1)
            if rez == '.':
                y1 += 1
        if x1 != self.x or y1 != self.y:

            return (x1, y1)
        return False

