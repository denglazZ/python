import sys
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

draw = False
start = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
            start = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if draw:
                position = event.pos
                width = position[0] - start[0]
                height = position[1] - start[1]
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1], width, height), 1)
                pygame.display.update()
            else:
                screen.fill((0, 0, 0))
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            draw = False

    clock.tick(30)