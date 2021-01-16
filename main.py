import pygame
from scripts.level import Level
from scripts.hero import Hero
from scripts.beat import Beat
from scripts.counter import Counter

if __name__ == '__main__':
    X_SIZE = 400
    Y_SIZE = 300

    pygame.init()
    size = width, height = X_SIZE, Y_SIZE
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    fps = 60
    clock = pygame.time.Clock()
    counter = Counter(fps)

    board = Level('data/levels/test_lvl')
    board.set_view(20)

    hero = Hero(counter, (5, 5), board)
    board.add_character(hero, (5, 5))
    beat = Beat(fps, counter)
    beat.set_geometry((300, 50), (50, 220))
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                hero.set_move(keys)
        counter.counter()
        board.render(screen)
        beat.render(screen)
        pygame.display.flip()
        clock.tick(fps)
