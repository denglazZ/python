import pygame
import random
w=800
h=800

screen=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()

game=True
draw = False
while game:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            startpos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0, 0, 0))
            draw = False
            pygame.display.update()
        if draw:
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                position = event.pos
                if (position[0] < startpos[0]):
                    pygame.draw.rect(screen, (255, 255, 255), (position[0], position[1], abs(position[0] - startpos[0]), abs(position[1] - startpos[1])))
                    pygame.display.update()
                if(position[1]<startpos[1]):
                    pygame.draw.rect(screen, (255, 255, 255), (position[0], startpos[1], abs(position[0] - startpos[0]), abs(position[1] - startpos[1])))
                    pygame.display.update()
                #pygame.draw.rect(screen, (255, 255, 255), (startpos[0], startpos[1], position[0] - startpos[0], position[1] - startpos[1]))





