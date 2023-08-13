import sys
import pygame
pygame.init()
Black = (0,0,0)

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
rect_x = 100
rect_y = 100
rect_size = 400
rect1_x = 50
rect1_y = 50
draw = False
start = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(Black)
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_size, rect_size))
    pygame.draw.rect(screen,(0,255,0),(rect_x+rect1_x,rect_y+rect1_y,100,100))
    pygame.draw.rect(screen,(0,0,0),(0,500,1000,200))
    #rect1_y += 3
    #rect_x += 5
    if(rect_x > 800):
        rect_x = -rect_size
    if(rect1_y > rect_size):
        rect1_y = rect_y-100
    pygame.display.flip()
    clock.tick(30)