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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 40
        self.image = pygame.Surface((50, self.width))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 500
        self.speedx = 0
        self.zader = pygame.time.Clock()
    def update(self):
        if keys[pygame.K_UP]:
            self.width += 3
        if keys[pygame.K_SPACE] and self.rect.y > 400:
            self.rect.y -= 5
        elif self.rect.y < 500:
            self.rect.y += 3

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.List = [RED,WHITE,GREEN]
        self.image = pygame.Surface((50, 200))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400 + random.randint(0,30)
        self.rect.bottom = 540
        self.speedx = 0
        self.zader = pygame.time.Clock()
    def update(self):
        self.rect.x -= 4
        if(self.rect.x < 0):
            self.rect.x = 400
            self.rect.y = random.randint(400,500)


all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
enemy = Enemy()

all_sprites.add(enemy)
enemy_group.add(enemy)
all_sprites.add(player)


running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    hits = pygame.sprite.spritecollide(player, enemy_group, False)

    all_sprites.update()

    screen.fill(BLACK)

    all_sprites.draw(screen)
    pygame.draw.rect(screen, BLACK, (0, 550, 600, 75))
    pygame.display.flip()
pygame.quit()