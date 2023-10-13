import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (225, 229, 180), (320, 240), 100)
    pygame.draw.circle(screen, (225, 229, 180), (420, 240), 100)
    pygame.draw.circle(screen,(225, 229, 180), (370, 150), 75)
    pygame.draw.circle(screen, (225, 229, 180), (370, 100), 75)
    pygame.draw.circle(screen, (225, 182, 193), (370, 75), 75)

    pygame.display.update()

pygame.quit