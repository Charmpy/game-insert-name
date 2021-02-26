import pygame
from scripts.container import Container
from scripts.door import Door
from scripts.enemy import Enemy
from scripts.graphics import Floor, Wall, Light

LEVELS = ['lvl_1']


class Level:
    def __init__(self, level, loop):
        self.loop = loop
        with open(level) as file:
            self.board = [list(i) for i in file.read().split('\n')]
        self.container = Container()
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.all_sprites = pygame.sprite.Group()
        self.create_fill()

    def create_fill(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 'd':
                    self.board[j][i] = Door((i, j), self)
                    self.container.add_character(self.board[j][i])
                    if i == 0:
                        self.container.add_spawn((1, j))
                    elif i == self.width - 1:
                        self.container.add_spawn((self.width - 2, j))
                    elif j == 0:
                        self.container.add_spawn((i, 1))
                    elif j == self.height - 1:
                        self.container.add_spawn((i, self.height - 2))
                elif self.board[j][i] == 'E':
                    target = self.loop.get_hero()
                    self.board[j][i] = Enemy(self.loop.counter, (i, j), self,
                                             target)
                    self.container.add_character(self.board[j][i])
                    Floor(self.left + self.cell_size * i + 1,
                          self.top + self.cell_size * j + 1, self.all_sprites)
                elif self.board[j][i] == '.':
                    Floor(self.left + self.cell_size * i + 1,
                          self.top + self.cell_size * j + 1, self.all_sprites)
                elif self.board[j][i] == '#':
                    Wall(self.left + self.cell_size * i + 1,
                          self.top + self.cell_size * j + 1, self.all_sprites)
                elif self.board[j][i] == 'F':
                    Light(self.left + self.cell_size * i + 1,
                          self.top + self.cell_size * j + 1, self.all_sprites)

    def get_spawns(self):
        return self.container.get_spawn()

    def set_view(self, cell_size):
        self.left = 10
        self.top = 10
        self.cell_size = cell_size

    def render(self, screen):
        self.container.update()
        self.all_sprites.draw(screen)
        for i in range(self.width):
            for j in range(self.height):
                # pygame.draw.rect(
                #     screen, pygame.Color('white'),
                #     (self.left + self.cell_size * i,
                #      self.top + self.cell_size * j,
                #      self.cell_size, self.cell_size), 1
                # )
                # if self.board[j][i] == '#':
                #     pygame.draw.rect(
                #         screen, pygame.Color('red'),
                #         (self.left + self.cell_size * i + 1,
                #          self.top + self.cell_size * j + 1,
                #          self.cell_size - 2, self.cell_size - 2)
                #     )
                # elif self.board[j][i] == '.':
                #     pygame.draw.rect(
                #         screen, pygame.Color('pink'),
                #         (self.left + self.cell_size * i + 1,
                #          self.top + self.cell_size * j + 1,
                #          self.cell_size - 2, self.cell_size - 2)
                #     )
                if self.board[j][i].__class__.__name__ == 'Hero':
                    self.board[j][i].draw(self.left + self.cell_size * i + 1,
                                          self.top + self.cell_size * j + 1)
                    # pygame.draw.rect(
                    #     screen, pygame.Color('blue'),
                    #     (self.left + self.cell_size * i + 1,
                    #      self.top + self.cell_size * j + 1,
                    #      self.cell_size - 2, self.cell_size - 2)
                    # )
                elif self.board[j][i].__class__.__name__ == 'Bullet':
                    # pygame.draw.rect(
                    #     screen, pygame.Color('pink'),
                    #     (self.left + self.cell_size * i + 1,
                    #      self.top + self.cell_size * j + 1,
                    #      self.cell_size - 2, self.cell_size - 2)
                    # )
                    self.board[j][i].draw(self.left + self.cell_size * i + 1,
                                          self.top + self.cell_size * j + 1)

                elif self.board[j][i].__class__.__name__ == 'Enemy':
                    pygame.draw.rect(
                        screen, pygame.Color('yellow'),
                        (self.left + self.cell_size * i + 1,
                         self.top + self.cell_size * j + 1,
                         self.cell_size - 2, self.cell_size - 2)
                    )
                elif self.board[j][i].__class__.__name__ == 'Door':
                    if self.board[j][i].is_open():
                        pass
                    else:
                        pygame.draw.rect(
                            screen, pygame.Color('gray'),
                            (self.left + self.cell_size * i + 1,
                             self.top + self.cell_size * j + 1,
                             self.cell_size - 2, self.cell_size - 2)
                        )

    def get_cell_info(self, x, y):
        return self.board[y][x]

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        return x, y

    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[y][x] = 1

    def get_click(self, mouse_pos):
        ee = self.get_cell(mouse_pos)
        if bool(ee):
            self.on_click(ee)

    def add_character(self, character, pos):
        x, y = pos
        self.board[y][x] = character
        self.container.add_character(character)

    def move_object(self, start_pos, target):
        x1, y1 = start_pos
        x2, y2 = target
        if self.board[y2][x2] == '.':
            self.board[y2][x2] = self.board[y1][x1]
            self.board[y1][x1] = '.'

    def clear_cell(self, pos):
        x, y = pos
        ide = id(self.board[y][x])
        self.container.delete_id(ide)
        self.board[y][x] = '.'

    def _get_structure(self):
        return self.board

    def change(self):
        self.loop.change()

    def all(self):
        self.loop.all()



