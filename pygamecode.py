import pygame
from pathlib import Path
from player import Player
from MyMissile import MyMissile

pygame.init()
screenHigh = 1000
screenWidth = 1720
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

keyCountX = 0
keyCountY = 0
Missiles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()
            if event.key == pygame.K_SPACE:
                m_x = player._x + 30
                m_y = player._y
                Missiles.append(MyMissile(xy=(m_x,m_y),playground=playground,sensitivity=movingScale))
                m_x = player._x + 80
                Missiles.append(MyMissile(playground,(m_x,m_y),movingScale))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1

    screen.blit(background,(0,0))
    Missiles = [item for item in Missiles if item._available]
    for m in Missiles:
        m.update()
        screen.blit(m._image,(m._x + 30,m._y))

    player.update()
    screen.blit(player._image, (player._x,player._y))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()