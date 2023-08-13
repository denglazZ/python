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
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 + random.randint(1,100)
        self.rect.bottom = HEIGHT / 2 + random.randint(1,100)
        self.speedx = 0
        self.zader = pygame.time.Clock()
    def update(self):
        self.move = 1
        self.k = random.randint(1,2)
        print(self.zader)
        if(self.k==1):
            self.rect.y -= 4
        if(self.k==2):
            self.rect.x += 4
        if self.rect.x > WIDTH:
            self.rect.x = WIDTH/2
        if self.rect.y < 0:
            self.rect.y = HEIGHT/2
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.y = 10

all_sprites = pygame.sprite.Group()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player = Player()
        all_sprites.add(player)

    pygame.draw.circle(screen, GREEN, (100, 100), 80)

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()