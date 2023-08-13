import pygame

class Player:
    def __init__(self, x: int, y: int, size: tuple):
        self.box = pygame.Surface(size)
        self.box.fill((0, 100, 0))
        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0
        self.y_speed = 0


    def move(self, right, left, up, down):
            if right:
                self.x_speed = 5
            if left:
                self.x_speed = -5
            if up:
                self.y_speed = -5
            if down:
                self.y_speed = 5
            if not (right or left or up or down):
                self.x_speed = 0
                self.y_speed = 0

            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
