import pygame
from random import*
pygame.init()
W = 400
H = 400
sc = pygame.display.set_mode((W, H))

class Game_sprite(pygame.sprite.Sprite):
    def __init__(self, x, filename,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha() 
        self.rect = self.image.get_rect(center=(x, 0)) 
        self.add(group)


cars=pygame.sprite.Group()
user_car=pygame.sprite.Group()
green_left=pygame.sprite.Group()
green_right=pygame.sprite.Group()
road_group=pygame.sprite.Group()

car1 = Game_sprite(100, 'Car1.png', user_car)
car2 = Game_sprite(randint(100,300), 'Car2.png', cars)
gr_left = Game_sprite(33, 'gr.png', green_left)
gr_right=Game_sprite(367, 'gr.png', green_right)
road=Game_sprite(200, 'road.png', road_group)
line_1 = Game_sprite(200, 'line.png', road_group)
line_2 = Game_sprite(200, 'line.png', road_group)

line_1.rect.y=0
line_2.rect.y=-400
car1.rect.y=200
car1.rect.x=100
car2.rect.y=0
gr_left.rect.y=0
gr_right.rect.y=0
road.rect.y=0

game=True
game_over=1
gr_vision = True
while game:
    keys = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
        elif keys[pygame.K_9]:
            game_over=1
            car2.rect.y = 0

    if game_over==1:
        
        if keys[pygame.K_LEFT]:
            car1.rect.x = car1.rect.x - 3
        elif keys[pygame.K_RIGHT]:
            car1.rect.x = car1.rect.x + 3
        elif keys[pygame.K_DOWN]:
            car1.rect.y = car1.rect.y + 3
        elif keys[pygame.K_UP]:
            car1.rect.y = car1.rect.y - 3

        sc.blit(road.image,road.rect)

        sc.blit(line_1.image,line_1.rect)
        sc.blit(line_2.image,line_2.rect)
        sc.blit(car1.image, car1.rect) 
        sc.blit(car2.image,car2.rect)
        if gr_vision == True:
            sc.blit(gr_left.image, gr_left.rect)
            sc.blit(gr_right.image,gr_right.rect)

        pygame.display.update()
        
        if car2.rect.y < H:
            car2.rect.y += 1
        else:
            car2 = Game_sprite(randint(100,300), 'Car2.png', cars)
            car2.rect.y = 0
            
        if line_1.rect.y < H:
            line_1.rect.y = line_1.rect.y + 2
        else:
            line_1 = Game_sprite(200, 'line.png', road_group)
            line_1.rect.y = -400
            
        if line_2.rect.y < H:
            line_2.rect.y = line_2.rect.y + 2
        else:
            line_2 = Game_sprite(200, 'line.png', road_group)
            line_2.rect.y = -400
        
        #if pygame.sprite.spritecollideany(car1, cars):
            #print("Авария!!!")
            #game_over=0

        if pygame.sprite.spritecollideany(car1,green_left):
            #car1.rect.x=car1.rect.x+5
            gr_vision == False
        
        if pygame.sprite.spritecollideany(car1,green_right):
            car1.rect.x=car1.rect.x-5


        
    
    