import pygame
from scripts.level import Level

if __name__ == '__main__':
    X_SIZE = 400
    Y_SIZE = 300

    pygame.init()
    size = width, height = X_SIZE, Y_SIZE
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))

    board = Level('data/levels/test_lvl')
    board.set_view(20)
    clock = pygame.time.Clock()
    running = True
    fps = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)



