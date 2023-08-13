import pygame
from random import*
pygame.init()
W = 400
H = 400
sc = pygame.display.set_mode((W, H))

class Game_sprite(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha() 
        self.rect = self.image.get_rect(center=(x, 0)) 

car1 = Game_sprite(randint(100,300), '../../py/Spped/Car2.png')
gr_left = Game_sprite(33, '../../py/Spped/gr.png')
gr_right=Game_sprite(367, '../../py/Spped/gr.png')
road=Game_sprite(200, 'road.png')
line_1 = Game_sprite(200, 'line.png')
line_2 = Game_sprite(200, 'line.png')

line_1.rect.y=0
line_2.rect.y=-400
car1.rect.y=0
gr_left.rect.y=0
gr_right.rect.y=0
road.rect.y=0

game=True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
    sc.blit(road.image,road.rect)
    sc.blit(gr_left.image, gr_left.rect)
    sc.blit(gr_right.image,gr_right.rect)
    sc.blit(line_1.image,line_1.rect)
    sc.blit(line_2.image,line_2.rect)
    sc.blit(car1.image, car1.rect) 

    pygame.display.update()

    if car1.rect.y < H:
        car1.rect.y = car1.rect.y + 2
    else:
        car1 = Game_sprite(randint(100,300), '../../py/Spped/Car2.png')
        car1.rect.y = 0
        
    if line_1.rect.y < H:
        line_1.rect.y = line_1.rect.y + 2
    else:
        line_1 = Game_sprite(200, 'line.png')
        line_1.rect.y = -400
        
    if line_2.rect.y < H:
        line_2.rect.y = line_2.rect.y + 2
    else:
        line_2 = Game_sprite(200, 'line.png')
        line_2.rect.y = -400
        
    
    