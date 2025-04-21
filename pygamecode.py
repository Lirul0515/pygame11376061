import pygame
from pathlib import Path

pygame.init()
screenHigh = 760
screenWidth = 1000
playground = [screenWidth,screenHigh]
screen = pygame.display.set_mode((screenWidth,screenHigh))

parent_path = Path(__file__).parent/'airplaneicon.png'
#image_path = parent_path/'gamecode'
#icon_path = image_path/'airplaneicon.png'

pygame.display.set_caption("1942偽")
icon_image = pygame.image.load(parent_path)
pygame.display.set_icon(icon_image)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))


screen = pygame.display.set_mode((screenWidth,screenHigh))
running = True
fps = 120
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()

