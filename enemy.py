from pathlib import Path
from typing import  Union
import pygame
from pygame.surface import Surface, SurfaceType
from gameObject import GameObject
import math
import random

class Enemy(GameObject):

    def __init__(self,playground, xy = None,sensitivity = 1,scale_factor = 0.1):
        GameObject.__init__(self,playground)
        self._moveScale = 0.5*sensitivity
        __parent__path = Path(__file__).parents[1]
        self.__enemy__path = __parent__path/'gamecode'/'res'/'airforce6.png'
        self._image = pygame.image.load(self.__enemy__path)
        original_width = self._image.get_rect().width
        original_height = self._image.get_rect().height
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self._image = pygame.transform.smoothscale(self._image, (new_width, new_height))
        self._center = self._x + self._image.get_rect().w/2,self._y + self._image.get_rect().h/2
        self._radius = 0.3*math.hypot(self._image.get_rect().w,self._image.get_rect().h)
        self._directionX = random.randint(-1,1)
        self._collided = False
        self._exploded = False
        self._available = True


        if xy is None:
            self._x = (self._playground[0] - self._image.get_rect().w)/2
            self._y = 3*self._playground[1]/40
        else:
            self._x = xy[0]
            self._y = xy[1]

        self._objectBound = (10,self._playground[0] - (self._image.get_rect().w + 10),10,self._playground[1] - (self._image.get_rect().h + 10))

    def update(self):
        self._y += self._moveScale/10
        self._x += self._directionX * self._moveScale
        if self._y > self._objectBound[3]:
            self._available = False
        if self._x < self._objectBound[0] or self._x > self._objectBound[1]:
            self._directionX *= -1
        GameObject.update(self)
        self._center = self._x + self._image.get_rect().w/2,self._y + self._image.get_rect().h/2

    def collision_detect(self,enemies):
        for enemy in enemies:
            if enemy is not self:
                self._hp -= 10
                self._collided = True
                enemy.hp = -1
                enemy.collided = True
                enemy.available = False