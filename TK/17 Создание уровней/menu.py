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


class Game_sprite(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))


def menu_def():
    sc.blit(menu.image, menu.rect)
    play = sc.blit(btn_start.image, btn_start.rect)
    stop = sc.blit(btn_stop.image, btn_stop.rect)
    pygame.display.update()

menu=Game_sprite(200, 'menu.png')
btn_start = Game_sprite(200, 'btn_play.png')
btn_stop = Game_sprite(200, 'btn_exit.png')

menu.rect.y = 0
btn_start.rect.y=150
btn_stop.rect.y=250

game=True
game_over=0

sc.blit(menu.image,menu.rect)
play=sc.blit(btn_start.image,btn_start.rect)
stop = sc.blit(btn_stop.image,btn_stop.rect)
pygame.display.update()

while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                pos=i.pos
                if play.collidepoint(pos):
                    game_over=1
                    k=14
                    f=42
                    s=0
                    pygame.display.update()
                elif stop.collidepoint(pos):
                    game=False