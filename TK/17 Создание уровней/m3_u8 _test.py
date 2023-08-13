import pygame
from random import*
pygame.init()
W = 400
H = 400
RED=(255,0,0)
sc = pygame.display.set_mode((W, H))
f=42
k=14
s=0
fp=100
lv=1

pygame.mixer.music.load('fon.mp3')
pygame.mixer.music.play(-1)
sound_udar = pygame.mixer.Sound('udar.wav')
sound_kanistra = pygame.mixer.Sound('udar_kanistra.wav')

class Game_sprite(pygame.sprite.Sprite):
    def __init__(self, x, filename,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha() 
        self.rect = self.image.get_rect(center=(x, 0)) 
        self.add(group)
        
def menu_def():
    sc.blit(menu.image,menu.rect)
    play = sc.blit(btn_start.image,btn_start.rect)
    stop = sc.blit(btn_stop.image,btn_stop.rect)
    pygame.display.update()

cars=pygame.sprite.Group()
user_car=pygame.sprite.Group()
green_left=pygame.sprite.Group()
green_right=pygame.sprite.Group()
road_group=pygame.sprite.Group()
canister_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
menu_group = pygame.sprite.Group()
play_group = pygame.sprite.Group()
stop_group = pygame.sprite.Group()

menu=Game_sprite(200, 'menu.png', menu_group)
btn_start = Game_sprite(200, 'btn_play.png', play_group)
btn_stop = Game_sprite(200, 'btn_exit.png', stop_group)

car1 = Game_sprite(100, 'Car1.png', user_car)
car2 = Game_sprite(randint(100,300), 'Car2.png', cars)

gr_left = Game_sprite(33, 'gr.png', green_left)
gr_right=Game_sprite(367, 'gr.png', green_right)

road=Game_sprite(200, 'road.png', road_group)

line_1 = Game_sprite(200, 'line.png', road_group)
line_2 = Game_sprite(200, 'line.png', road_group)

canister=Game_sprite(randint(100,300), 'canister.png', canister_group)
fuel=Game_sprite(365, 'fuel.png', fuel_group)

level_2_left=Game_sprite(33, 'afrika_l.png', green_left)
level_2_right=Game_sprite(367, 'afrika_r.png', green_right)

level_3_left=Game_sprite(33, 'pesok.png', green_left)
level_3_right=Game_sprite(367, 'pesok.png', green_right)

level_4_left=Game_sprite(33, 'gorod_l.png', green_left)
level_4_right=Game_sprite(367, 'gorod_r.png', green_right)

level_5_left=Game_sprite(33, 'gora_l.png', green_left)
level_5_right=Game_sprite(367, 'gora_r.png', green_right)

line_1.rect.y=0
line_2.rect.y=-400
car1.rect.y=200
car1.rect.x=100
car2.rect.y=0
gr_left.rect.y=0
gr_right.rect.y=0
road.rect.y=0
canister.rect.y=0
fuel.rect.y=20
menu.rect.y = 0
btn_start.rect.y=150
btn_stop.rect.y=250
level_2_left.rect.y=0
level_2_right.rect.y=0
level_3_left.rect.y=0
level_3_right.rect.y=0
level_4_left.rect.y=0
level_4_right.rect.y=0
level_5_left.rect.y=0
level_5_right.rect.y=0

game=True
game_over=0

sc.blit(menu.image,menu.rect)
play=sc.blit(btn_start.image,btn_start.rect)
stop = sc.blit(btn_stop.image,btn_stop.rect)
pygame.display.update()

while game:
    keys = pygame.key.get_pressed()
    score=pygame.font.Font(None,46)
    text_score=score.render(str(s),1,(255,255,255))

    per=pygame.font.Font(None,18)
    text_per = per.render(str(fp),1,(255,255,255))

    level=pygame.font.Font(None,25)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                pos=i.pos
                if play.collidepoint(pos):
                    game_over=1
                    car2.rect.y = 0
                    k=14
                    f=42
                    s=0
                    lv=1
                    pygame.display.update()
                elif stop.collidepoint(pos):
                    game=False

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
        sc.blit(gr_left.image, gr_left.rect)
        sc.blit(gr_right.image,gr_right.rect)
        sc.blit(line_1.image,line_1.rect)
        sc.blit(line_2.image,line_2.rect)
        sc.blit(car1.image, car1.rect) 
        sc.blit(car2.image,car2.rect)
        pygame.draw.rect(sc,RED, (346,14+k,22,f))
        sc.blit(canister.image,canister.rect)
        sc.blit(fuel.image,fuel.rect)
        sc.blit(text_score,(20,30))
        sc.blit(text_per,(347,30))

        pygame.display.update()

        f=f-0.03
        k=k+0.03
        fp=int(f*2.4)

        if car2.rect.y < H:
            car2.rect.y = car2.rect.y + randint(lv,lv+2)
        else:
            car2 = Game_sprite(randint(100,300), 'Car2.png', cars)
            car2.rect.y = 0
            s=s+1
            text_score=score.render(str(s),1,(255,255,255))

        if s<10:
            text_level=level.render("Level "+str(lv),1,(255,255,255))
            sc.blit(text_level,(5,370))

            pygame.display.update()

        if s>=10 and s<20:
            lv=2
            text_level=level.render("Level "+str(lv),1,(255,255,255))
            sc.blit(level_2_left.image, level_2_left.rect)
            sc.blit(level_2_right.image,level_2_right.rect)
            pygame.draw.rect(sc,RED, (346,14+k,22,f))
            sc.blit(canister.image,canister.rect)
            sc.blit(fuel.image,fuel.rect)
            sc.blit(text_score,(20,30))
            sc.blit(text_per,(347,30))
            sc.blit(text_level,(5,370))

            pygame.display.update()
        
        if s>=20 and s<30:
            lv=3
            text_level=level.render("Level "+str(lv),1,(255,255,255))
            sc.blit(level_3_left.image, level_3_left.rect)
            sc.blit(level_3_right.image,level_3_right.rect)
            pygame.draw.rect(sc,RED, (346,14+k,22,f))
            sc.blit(canister.image,canister.rect)
            sc.blit(fuel.image,fuel.rect)
            sc.blit(text_score,(20,30))
            sc.blit(text_per,(347,30))
            sc.blit(text_level,(5,370))

            pygame.display.update()

        if s>=30 and s<40:
            lv=4
            text_level=level.render("Level "+str(lv),1,(255,0,0))
            sc.blit(level_4_left.image, level_4_left.rect)
            sc.blit(level_4_right.image,level_4_right.rect)
            pygame.draw.rect(sc,RED, (346,14+k,22,f))
            sc.blit(canister.image,canister.rect)
            sc.blit(fuel.image,fuel.rect)
            sc.blit(text_score,(20,30))
            sc.blit(text_per,(347,30))
            sc.blit(text_level,(5,370))
        
            pygame.display.update()
        if s>=40:
            lv=5
            text_level=level.render("Level "+str(lv),1,(255,255,255))
            sc.blit(level_5_left.image, level_5_left.rect)
            sc.blit(level_5_right.image,level_5_right.rect)
            pygame.draw.rect(sc,RED, (346,14+k,22,f))
            sc.blit(canister.image,canister.rect)
            sc.blit(fuel.image,fuel.rect)
            sc.blit(text_score,(20,30))
            sc.blit(text_per,(347,30))
            sc.blit(text_level,(5,370))
        
            pygame.display.update()  

        if line_1.rect.y < H:
            line_1.rect.y = line_1.rect.y + 2
        else:
            line_1 = Game_sprite(200, 'line.png', road_group)
            line_1.rect.y = -400
            
        if line_2.rect.y < H :
            line_2.rect.y = line_2.rect.y + 2
        else:
            line_2 = Game_sprite(200, 'line.png', road_group)
            line_2.rect.y = -400
        
        if canister.rect.y<H:
            canister.rect.y=canister.rect.y+2

        else:
            canister.rect.y=0-randint(200,1000) 

        if pygame.sprite.spritecollideany(car1,canister_group):
            canister.rect.y=0-randint(200,1000)
            sound_kanistra.play()
            k=14
            f=42
            
        if f<0:
            game_over=0
            menu_def()

        if pygame.sprite.spritecollideany(car1, cars): 
            print("Авария!!!")
            sound_udar.play()
            game_over=0
            pygame.time.delay(2000)
            menu_def()

        if pygame.sprite.spritecollideany(car1,green_left):
            car1.rect.x=car1.rect.x+5
        
        if pygame.sprite.spritecollideany(car1,green_right):
            car1.rect.x=car1.rect.x-5


        
    
    