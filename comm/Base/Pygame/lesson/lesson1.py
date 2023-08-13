import pygame
width=400
height=400
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
game=True
while game:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        elif event.type == pygame.MOUSEMOTION:
            print(f"Координаты курсора мыши: {event.pos}")
            print(f"Смещение курсора мыши относительно предыдущего положения: {event.rel}")

    screen.fill((0, 255, 0))
    pygame.display.update()