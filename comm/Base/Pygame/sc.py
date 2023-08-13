import pygame
from random import *

w = 800
h = 600

possnake = [w//2,h//2]

posapple = [300,500]

sc = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

game = True

snakespeed = [0,0]
blocksize = 20


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakespeed = [-blocksize,0]
            if event.key == pygame.K_RIGHT:
                snakespeed = [blocksize,0]
            if event.key == pygame.K_UP:
                snakespeed = [0,-blocksize]
            if event.key == pygame.K_DOWN:
                snakespeed = [0,blocksize]
    sc.fill((150,75,0))
    pygame.draw.rect(sc,(0,255,0),(possnake[0],possnake[1],blocksize,blocksize))
    pygame.draw.rect(sc,(255,0,0),(posapple[0],posapple[1],blocksize,blocksize))
    pygame.display.update()
    possnake[0] += snakespeed[0]
    possnake[1] += snakespeed[1]
    if(possnake[0] == posapple[0] and possnake[1] == posapple[1]):
        posapple[0] = (randint(0,w)//blocksize) * blocksize
        posapple[1] = (randint(0,h)//blocksize) * blocksize
    if possnake[0] >= w:
        possnake[0] = 0
    clock.tick(blocksize)