import pygame
import random

Width = 800
Height = 800
sc = pygame.display.set_mode((Width,Height))

Green = (0,255,0)
clock = pygame.time.Clock()

x=300
y=300

snake_block = 10
snake_speed = 15

x1=round(random.randrange(0, Width - snake_block) / 10.0) * 10.0
y1=round(random.randrange(0, Height - snake_block) / 10.0) * 10.0

left,right,up,down=False,False,False,False

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    sc.fill((0,0,0))
    pygame.draw.rect(sc, (255, 255, 255), (x, y, snake_block, snake_block))
    pygame.draw.rect(sc, (255, 255, 255), (x1, y1, snake_block, snake_block))

    pygame.display.update()
    clock.tick(30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
        right, up, down = False, False, False
    if keys[pygame.K_RIGHT]:
        right = True
        left, up, down = False, False, False
    if keys[pygame.K_DOWN]:
        down = True
        right, up, left = False, False, False
    if keys[pygame.K_UP]:
        up = True
        right, left, down = False, False, False
    if left:
        x -= snake_block
    if right:
        x += snake_block
    if down:
        y += snake_block
    if up:
        y -= snake_block
    if(x ==x1 and y == y1):
        x1 = round(random.randrange(0, Width - snake_block) / 10.0) * 10.0
        y1 = round(random.randrange(0, Height - snake_block) / 10.0) * 10.0

