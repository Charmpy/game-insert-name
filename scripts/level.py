import pygame


class Level:
    def __init__(self, level):
        with open(level) as file:
            self.board = [list(i) for i in file.read().split('\n')]

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.width = len(self.board[0])
        self.height = len(self.board)

    def set_view(self, cell_size):
        self.left = (400 - cell_size * self.width) // 2
        self.top = 10
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(
                    screen, pygame.Color('white'),
                    (self.left + self.cell_size * i,
                     self.top + self.cell_size * j,
                     self.cell_size, self.cell_size), 1
                )

                if self.board[j][i] == '#':
                    pygame.draw.rect(
                        screen, pygame.Color('red'),
                        (self.left + self.cell_size * i + 1,
                         self.top + self.cell_size * j + 1,
                         self.cell_size - 2, self.cell_size - 2)
                    )
                elif self.board[j][i].__class__.__name__ == 'Hero':
                    pygame.draw.rect(
                        screen, pygame.Color('blue'),
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

    def move_character(self, start_pos, target):
        x1, y1 = start_pos
        x2, y2 = target
        (self.board[y1][x1], self.board[y2][x2]) = (
            self.board[y2][x2], self.board[y1][x1]
        )

    def _get_structure(self):
        return self.board

