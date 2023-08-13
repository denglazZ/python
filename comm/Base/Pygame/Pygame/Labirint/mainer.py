from level import data,data2
from blocks import Box
from player import Player
import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

right = left = up = down = False

pygame.init()
size = width, height = len(data[0]) * 32, len(data) * 32
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()

level = 1

box_x = 0
box_y = 0
box_list = []
for i in data:
    for j in i:
        if(j == "1"):
            box_list.append(Box(box_x,box_y,(32,32)))
        box_x += 32
    box_y += 32
    box_x = 0

box_x = 0
box_y = 0
box_list2 = []
for i in data2[0]:
    if(i == "1"):
        box_list2.append(Box(box_x,box_y,(32,32)))
    box_x += 32


Player = Player(64, 64, (32, 64))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            up = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            down = True

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            up = False
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            down = False

    screen.fill((0, 0, 0))
    if(level == 1):
        for i in box_list:
            screen.blit(i.box, (i.rect.x, i.rect.y))
    elif(level == 2):
        for i in box_list2:
            screen.blit(i.box, (i.rect.x, i.rect.y))

    Player.move(right, left, up, down)

    # отображение игрока на экране
    screen.blit(Player.box, (Player.rect.x, Player.rect.y))
    if(Player.rect.x > 400):
        level = 2
        print("level 2")
    pygame.display.update()

    clock.tick(60)

