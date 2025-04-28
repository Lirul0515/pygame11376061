import pygame
from pathlib import Path
from player import Player

pygame.init()
screenHigh = 760
screenWidth = 1000
playground = [screenWidth,screenHigh]
screen = pygame.display.set_mode((screenWidth,screenHigh))

parent_path = Path(__file__).parent/'res'/'airplaneicon.png'
image_path = parent_path/'gamecode'
icon_path = image_path/'airplaneicon.png'

pygame.display.set_caption("1942偽")
icon_image = pygame.image.load(parent_path)
pygame.display.set_icon(icon_image)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((150,150,150))

screen = pygame.display.set_mode((screenWidth,screenHigh))
running = True
fps = 120
movingScale = 600/fps

player = Player(playground = playground, sensitivity = movingScale)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    player.update()
    screen.blit(player._image, (player._x,player._y))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()