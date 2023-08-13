import pygame
pygame.init()
W = 400
H = 400
WHITE = (255, 0, 255)
sc = pygame.display.set_mode((W, H))

class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Car.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

car1 = Car(100, 'Car.png')
car1.rect.y = 100
game=True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print("Exit")
            game=False
    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pygame.display.update()

    if car1.rect.y < H:
        car1.rect.y += 5
    else:
        car1.rect.y = 90
        car1 = Car(100, 'Car1.png')