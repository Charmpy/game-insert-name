from scripts.character import Character
from scripts.graphics import CharacterSprt
from random import choice

ENEMIES = [['enemy90_1.png', 'enemy45_1.png'],
           ['enemy90_2.png', 'enemy45_2.png']]


class Enemy(Character):
    def __init__(self, counter, pos, level, target, direction='r'):
        super().__init__(counter, pos, level, direction)
        self.target = target
        self.delay = 2
        self.ticks = 0
        rez = choice(ENEMIES)
        self.sprite = CharacterSprt(
            level.move_sprites, rez[0], rez[1]
        )

    def __repr__(self):
        return 'E'

    def get_sprite(self):
        return self.sprite

    def draw(self, x, y):
        self.sprite.update(x, y)

    def move_logic(self):
        if abs(self.counter.get_bpm() - self.counter.get_counter()) == 0:
            self.ticks += 1
            if self.ticks == self.delay:
                self.ticks = 0
                x, y = self.target.get_coords()

                if self.x == x:
                    if self.y < y:
                        self.set_direction('d')
                    elif self.y > y:
                        self.set_direction('u')
                elif self.y == y:
                    if self.x < x:
                        self.set_direction('r')
                    elif self.x > x:
                        self.set_direction('l')
                else:
                    if self.x < x and self.y < y:
                        self.set_direction('dr')
                    elif self.x < x and self.y > y:
                        self.set_direction('ur')
                    elif self.x > x and self.y > y:
                        self.set_direction('ul')
                    elif self.x > x and self.y < y:
                        self.set_direction('dl')
                if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
                    self.level.clear_cell((x, y))
                    self.level.all()
                self.move()
            self.sprite.rotate(self.direct)



