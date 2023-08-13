import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Randmove")
clock = pygame.time.Clock()

draw = False
start = 0
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
            start = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if draw:
                position = event.pos
                width = start[0] - position[0]
                height = start[1] - position[1]
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, (255, 255, 255), (position[0], position[1], width, height), 1)
                pygame.display.update()
            else:
                screen.fill((0, 0, 0))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            draw = False

    pygame.draw.rect(screen, BLUE, (40, 550, 600, 75))
    pygame.display.flip()
pygame.quit()