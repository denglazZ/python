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

car1 = Game_sprite(100, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/Car1.png')
car2 = Game_sprite(randint(100,300),
                   '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/Car2.png')
gr_left = Game_sprite(33, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/gr.png')
gr_right=Game_sprite(367, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/gr.png')
road=Game_sprite(200, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/road.png')
line_1 = Game_sprite(200, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/line.png')
line_2 = Game_sprite(200, '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/line.png')


line_1.rect.y=0
line_2.rect.y=-400
car1.rect.y=100
car1.rect.x=100
car2.rect.y=0
car2.rect.x=0
gr_left.rect.y=0
gr_right.rect.y=0
road.rect.y=0


game=True

while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        car1.rect.x = car1.rect.x - 3
    elif keys[pygame.K_RIGHT]:
        car1.rect.x = car1.rect.x + 3
    elif keys[pygame.K_DOWN]:
        car1.rect.y = car1.rect.y + 3
    elif keys[pygame.K_UP]:
        car1.rect.y = car1.rect.y - 3

    sc.blit(road.image,road.rect)
    sc.blit(gr_left.image, gr_left.rect)
    sc.blit(gr_right.image,gr_right.rect)
    sc.blit(line_1.image,line_1.rect)
    sc.blit(line_2.image,line_2.rect)
    sc.blit(car1.image, car1.rect) 
    sc.blit(car2.image,car2.rect)

    pygame.display.update()

    if car2.rect.y < H:
        car2.rect.y = car2.rect.y + randint(1, 2)
    else:
        car2 = Game_sprite(randint(100,300),
                           '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/Car2.png')
        car2.rect.y = 0
        
    if line_1.rect.y < H:
        line_1.rect.y = line_1.rect.y + 2
    else:
        line_1 = Game_sprite(200,
                             '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/line.png')
        line_1.rect.y = -400
        
    if line_2.rect.y < H:
        line_2.rect.y = line_2.rect.y + 2
    else:
        line_2 = Game_sprite(200,
                             '../14 Взаимодействие спрайтов. Продолжение. Создание зависимых элементов игры/line.png')
        line_2.rect.y = -400

        
    
    