import pygame
from pathlib import Path
from player import Player
from MyMissile import MyMissile
from enemy import Enemy

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
enemy = Enemy(playground = playground, sensitivity = movingScale)

clock = pygame.time.Clock()

keyCountX = 0
keyCountY = 0
Missiles = []
launchMissile = pygame.USEREVENT + 1
enemies = []
launchEnemy = pygame.USEREVENT + 2
pygame.time.set_timer(launchEnemy,2000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == launchMissile:
            m_x = player._x - 60
            m_y = player._y
            Missiles.append(MyMissile(xy=(m_x,m_y),playground=playground,sensitivity=movingScale))
            m_x = player._x + 80
            Missiles.append(MyMissile(xy=(m_x,m_y),playground=playground,sensitivity=movingScale))
        if event.type == launchEnemy:
            enemy._x = enemy._x
            enemy._y = enemy._y
            enemies.append(Enemy(xy=(enemy._x,enemy._y),playground=playground,sensitivity=movingScale))
            enemy._x = enemy._x
            enemies.append(Enemy(xy=(enemy._x,enemy._y),playground=playground,sensitivity=movingScale))

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
                m_x = player._x - 60
                m_y = player._y
                Missiles.append(MyMissile(xy=(m_x,m_y),playground=playground,sensitivity=movingScale))
                m_x = player._x + 80
                Missiles.append(MyMissile(playground,(m_x,m_y),movingScale))
                pygame.time.set_timer(launchMissile,400)


        if event.type == launchEnemy:
            enemy._x = screenWidth/2
            enemy._y = -100
            enemies.append(Enemy(xy=(enemy._x - 40,enemy._y ),playground=playground,sensitivity=movingScale))
            enemies.append(Enemy(xy=(enemy._x + 40,enemy._y),playground=playground,sensitivity=movingScale))
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
            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile,0)

    screen.blit(background,(0,0))
    Missiles = [item for item in Missiles if item._available]
    enemies = [item for item in enemies if item._available]
    for m in Missiles:
        m.update()
        screen.blit(m._image,(m._x + 59,m._y + 60))
    for enemy in enemies:
        enemy.update()
        screen.blit(enemy._image,(enemy._x ,enemy._y ))
    player.update()
    screen.blit(player._image, (player._x,player._y))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()