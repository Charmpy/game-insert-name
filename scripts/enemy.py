from scripts.character import Character


class Enemy(Character):
    def __init__(self, counter, pos, level, direction='r'):
        super().__init__(counter, pos, level, direction)

    def __repr__(self):
        return 'E'
