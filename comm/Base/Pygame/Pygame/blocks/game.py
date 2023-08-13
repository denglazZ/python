import pygame
import math
from random import *

pygame.init()
W = 1000
H = 1000
RED = (255, 0, 0)
f = 42
k = 14
sc = pygame.display.set_mode((W, H))
position = pygame.math.Vector2(sc.get_rect().center)
direction = pygame.math.Vector2(5, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

    def rotate(self,filename):
         mouse_x, mouse_y = pygame.mouse.get_pos()
         rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
         angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
         self.image = pygame.transform.rotate(pygame.image.load(filename), int(angle))

hero = Player(200, "car1.PNG")
hero.rect.y = 400
hero.rect.x = 500

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        position += direction
    if keys[pygame.K_s]:
        position -= direction
    sc.fill(RED)
    sc.blit(hero.image, hero.rect)
    angle = direction.angle_to((1, 0))
    rotated_car = pygame.transform.rotate(hero, angle)
    sc.blit(rotated_car, rotated_car.get_rect(center=(round(position.x), round(position.y))))
    hero.rotate("Car1.PNG")
    pygame.display.update()






