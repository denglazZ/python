import pygame
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
game = True
y = 200
count = 0
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((255,0,0))
    pygame.draw.rect(screen,(0,255,0),(200,y,200,50))
    pygame.display.update()
    y += 10
    count+=1
    print(count)
    clock.tick(20)