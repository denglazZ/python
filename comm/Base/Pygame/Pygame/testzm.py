import pygame
FPS = 144
W = 800
H = 800
red = (213, 50, 80)
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

pygame.font.init()

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    sc.fill((0,0,0))
    pygame.draw.rect(sc,(0,255,0),(100,100,-100,-100))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)






