import pygame

pygame.init()


fps = 60
clock = pygame.time.Clock()
WIDTH = 400
HEIGHT = 400
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill((0,0,0))
    LIGHT_BLUE = (3, 169, 244)
    BLUE_GREY = (96, 125, 139)

    for i in range(WIDTH // 40):
        pygame.draw.rect(screen, LIGHT_BLUE, (i * 40, 0, 40, 40))
        pygame.draw.rect(screen, BLUE_GREY, (i * 40 + 3, 3, 34, 34))

    pygame.display.update()


