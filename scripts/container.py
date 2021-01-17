class Container:
    def __init__(self):
        self.container = []

    def add_character(self, character):
        self.container.append(character)

    def update(self):

        for i in range(len(self.container)):
            if self.container[i].__class__.__name__ == 'Bullet':
                self.container[i].set_move()
