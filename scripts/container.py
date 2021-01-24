class Container:
    def __init__(self):
        self.container = []
        self.enemies = 0

    def add_character(self, character):
        self.container.append(character)

    def update(self):
        k = 0
        for i in self.container:
            if i.__class__.__name__ == 'Bullet':
                i.set_move()
            if i.__class__.__name__ == 'Enemy':
                k += 1
                i.move_logic()
            if i.__class__.__name__ == 'Door':
                i.is_open()
        self.enemies = k

    def enemy_count(self):
        return self.enemies

    def get_list(self):
        return self.container

    def delete_id(self, ide):
        for i in range(len(self.container)):
            if id(self.container[i]) == ide:
                del self.container[i]
                break

