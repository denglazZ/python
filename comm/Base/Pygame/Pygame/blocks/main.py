from level import data
from block import Box
from player import Hero
from monetka import Monetka

import sys
import pygame
pygame.init()

size = width, height = len(data[0]) * 32, len(data) * 32

# переменные для проверки касания игрока с препятствиями
right = left = up = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

money1 = Monetka(96,96,(32,32))
### создание уровня ###
box_x = box_y = 0     # начальные координаты первой поверхности
box_list = []         # список для хранения поверхностей
for i in data:
    for j in i:
        if j == "1":
            box_list.append(Box(box_x, box_y, (32, 32)))
        box_x += 32
    box_x = 0
    box_y += 32
### создание уровня ###

player_01 = Hero(64, 64, (32, 64))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            up = True

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            up = False

    # цикл для отображения поверхностей на экране
    for i in box_list:
        screen.blit(i.box, (i.rect.x, i.rect.y))

    if (player_01.rect.x < money1.rect.x):
        screen.blit(money1.circle,(money1.rect.x,money1.rect.y))

    player_01.move(right, left, up, box_list)

    # отображение игрока на экране
    screen.blit(player_01.box, (player_01.rect.x, player_01.rect.y))
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)
