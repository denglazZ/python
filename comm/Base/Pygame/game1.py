import sys
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

player = pygame.Surface((50, 50))
player.fill((255, 0, 0))
player_rect = player.get_rect()

player_rect.x = 500
player_rect.y = 200

enemy = pygame.Surface((100,100))
enemy.fill((0,255,0))
enemy_rect = enemy.get_rect()

enemy_rect.x = 100
enemy_rect.y = 150

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill((0, 0, 0))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)
    pygame.display.update()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 10
    if keys[pygame.K_RIGHT]:
        player_rect.x += 10

