import pygame
import time
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
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.Jumpper = False

    def update(self):
        self.speedx = 0
        self.rect.y += 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.y = 10
        if (self.Jumpper):
            self.rect.y -= 10


class Platform(pygame.sprite.Sprite):
    def __init__(self, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, WIDTH)
        self.rect.y = 100 * a
        self.speedy = random.randrange(1, 8)
    def update(self):
        if self.rect.y > WIDTH:
            self.rect.y = random.randrange(10,30)
            self.rect.x = random.randrange(10, WIDTH)
        if player.rect.y < WIDTH//2:
            self.rect.y += 3

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    pl = Platform(i)
    all_sprites.add(pl)
    mobs.add(pl)
a = 0
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hits = pygame.sprite.spritecollide(player, mobs,False,False)
    if hits:
        a = player.rect.y
        player.Jumpper = True
    if(player.Jumpper and (a - 250 > player.rect.y)):
        player.Jumpper = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()