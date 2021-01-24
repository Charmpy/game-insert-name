class Door:
    def __init__(self, pos, level):
        self.x, self.y = pos
        self.level = level

    def is_open(self):
        lst = self.level.container. enemy_count()
        if lst > 0:
            return False
        return True

    def __repr__(self):
        return 'D'

