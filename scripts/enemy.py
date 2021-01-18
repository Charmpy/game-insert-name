from scripts.character import Character


class Enemy(Character):
    def __init__(self, counter, pos, level, target, direction='r'):
        super().__init__(counter, pos, level, direction)
        self.target = target
        self.delay = 2
        self.ticks = 0

    def __repr__(self):
        return 'E'

    def move_logic(self):
        if abs(self.counter.get_bpm() - self.counter.get_couter()) == 0:
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
                self.move()
