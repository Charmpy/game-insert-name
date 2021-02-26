import pygame
from scripts.main_loop import MainLoop
from scripts.beat import Beat
from scripts.counter import Counter
from scripts.music import Music
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    X_SIZE = 470
    Y_SIZE = 600

    pygame.init()
    size = width, height = X_SIZE, Y_SIZE
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    fps = 50
    clock = pygame.time.Clock()


    def terminate():
        pygame.quit()
        sys.exit()


    def start_screen():
        intro_text = ["BEGIN"]

        fon = pygame.transform.scale(load_image('fon.gif'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру
            pygame.display.flip()
            clock.tick(fps)

    def end_screen():
        intro_text = ["END"]

        fon = pygame.transform.scale(load_image('fon.gif'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру
            pygame.display.flip()
            clock.tick(fps)

    while True:
        counter = Counter(fps)
        music = Music(counter)
        main_loop = MainLoop(counter, music)
        beat = Beat(fps, counter)
        beat.set_geometry((450, 50), (10, 500))
        start_screen()
        music.start()

        while running:
            music.play()
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    main_loop.action(keys)
            if main_loop.check():
                break
            counter.counter()
            main_loop.render(screen)
            beat.render(screen)
            pygame.display.flip()
            clock.tick(fps)
        end_screen()
