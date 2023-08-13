import pygame
import random
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)

W = 400
H = 700
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.rect.centerx = W / 2
        self.rect.bottom = H / 2
        self.speedx = 0
    def update(self):
        self.speedx = 0
        self.rect.y += 1
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > H:
            self.rect.y = 10
    def jump(self):
        self.rect.y -= 100

class Platform(pygame.sprite.Sprite):
    def __init__(self, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 10))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, W)
        self.rect.y = 100 * a
        self.speedy = random.randrange(1, 8)
    def update(self):
        if self.rect.y > W:
            self.rect.y = random.randrange(10,30)
            self.rect.x = random.randrange(10, W)
        if player.rect.y < W//2:
            self.rect.y += 1


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    pl = Platform(i)
    all_sprites.add(pl)
    mobs.add(pl)

x = W/2
right_move = True
left_move = False
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    sc.fill(White)
    all_sprites.draw(sc)
    all_sprites.update()
    #print(player.rect.x)
    #pygame.draw.circle(sc,(Green),(x, H/2),(100))
    #if right_move:
    #    x += 1
    #    if x > W:
    #        right_move = False
    #        left_move = True
    #if left_move:
    #    x -= 1
    #    if x < 0:
    #        right_move = True
    #        left_move = False

    pygame.display.update()
    clock.tick(120)