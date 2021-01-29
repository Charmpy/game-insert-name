import pygame
from scripts.main_loop import MainLoop
from scripts.beat import Beat
from scripts.counter import Counter
from scripts.enemy import Enemy


if __name__ == '__main__':
    X_SIZE = 400
    Y_SIZE = 400

    pygame.init()
    size = width, height = X_SIZE, Y_SIZE
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    fps = 60
    clock = pygame.time.Clock()
    counter = Counter(fps)
    main_loop = MainLoop(counter)
    beat = Beat(fps, counter)
    beat.set_geometry((300, 50), (50, 320))
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                main_loop.action(keys)
        counter.counter()
        main_loop.render(screen)
        beat.render(screen)
        pygame.display.flip()
        clock.tick(fps)
