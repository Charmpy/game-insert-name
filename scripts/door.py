from scripts.graphics import DoorSprt


class Door:
    def __init__(self, pos, level):
        self.x, self.y = pos
        self.level = level
        self.sprite = DoorSprt(self.level.all_sprites, False)
        self.is_open()

    def draw(self, x, y):
        self.is_open()
        self.sprite.update(x, y)

    def is_open(self):
        lst = self.level.container.enemy_count()
        if lst > 0:
            self.sprite.set_mode(False)
            return False
        self.sprite.set_mode(True)
        return True

    def __repr__(self):
        return 'D'

    def teleport(self):
        if self.is_open():
            self.level.change()

