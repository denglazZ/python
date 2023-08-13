import pygame
pygame.init()


class Box:
    def __init__(self, x: int, y: int, size: tuple):
        self.box = pygame.Surface(size)
        self.box.fill((100, 0, 0))
        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y

