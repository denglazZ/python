import pygame

class Player:
    def __init__(self, x: int, y: int, size: tuple):
        self.box = pygame.Surface(size)
        self.box.fill((0, 100, 0))
        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y


WIDTH = 480
HEIGHT = 600
FPS = 60

right = left = up = down = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(100,100,(50,50))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
    elif keys[pygame.K_RIGHT]:
        right = True
    elif keys[pygame.K_DOWN]:
        down = True
    elif keys[pygame.K_UP]:
        up = True
    else:
        right = left = up = down = False
    if right:
        player.rect.x += 5
    if left:
        player.rect.x -= 5
    if up:
        player.rect.y -= 5
    if down:
        player.rect.y += 5
    screen.blit(player.box, (player.rect.x, player.rect.y))
    pygame.display.update()
    clock.tick(60)

