import pygame
pygame.init()


class Monetka:
    def __init__(self, x: int, y: int, size: tuple):
        self.circle = pygame.Surface(size)
        self.circle.fill((255, 215, 0))
        self.rect = self.circle.get_rect()
        self.rect.x = x
        self.rect.y = y

