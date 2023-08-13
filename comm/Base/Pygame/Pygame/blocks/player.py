from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
from operator import le
import pygame
pygame.init()


class Hero:
    def __init__(self, x: int, y: int, size: tuple):
        self.box = pygame.Surface(size)
        self.box.fill((0, 100, 0))
        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.on_ground = False  # игрок на земле? (Да/Нет)
        self.x_speed = 0        # скорость перемещения игрока по оси X
        self.y_speed = 0        # скорость перемещения игрока по оси Y
        self.jump = False

    def move(self, right, left, up, box_list):
        if right:
            self.x_speed = 5
        if left:
            self.x_speed = -5
        if not (right or left):
            self.x_speed = 0

        if not self.jump:
            if up:
                self.y_speed = -20
                self.jump = True

        if not self.on_ground:
            self.y_speed += 1
        self.on_ground = False

        self.rect.x += self.x_speed
        self.collision(self.x_speed, 0, box_list)
        self.rect.y += self.y_speed
        self.collision(0, self.y_speed, box_list)


    def collision(self, x, y, box_list):  # box_list - список объектов
        for i in box_list:
            if self.rect.colliderect(i.rect):
                if x > 0:
                    self.rect.right = i.rect.left
                if x < 0:
                    self.rect.left = i.rect.right
                if y > 0:
                    self.rect.bottom = i.rect.top
                    self.y_speed = 0
                    self.on_ground = True
                    self.jump = False
                if y < 0:
                    self.rect.top = i.rect.bottom
                    self.y_speed = 0
