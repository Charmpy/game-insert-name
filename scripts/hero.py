from scripts.character import Character


class Hero(Character):
    def __init__(self, counter, pos, level, direction='r'):
        super().__init__(counter, pos, level, direction)

    def set_move(self, key):
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


