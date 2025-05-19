from pathlib import Path
from typing import  Union
import pygame
from pygame.surface import Surface, SurfaceType
from gameObject import GameObject
import math

@property
def hp(self):
    return self._hp

@hp.setter
def hp(self, value):
    self._hp = max(0, value)  # 不允許負數血量
    if self._hp == 0:
        self._alive = False
        self._available = False  # 可選，觸發死亡動畫等

@property
def alive(self):
    return self._alive

@alive.setter
def alive(self, value):
    self._alive = value

class Player(GameObject):

    def __init__(self,playground, xy = None,sensitivity = 1,scale_factor = 0.2):
        GameObject.__init__(self,playground)
        self._moveScale = 0.5*sensitivity
        self._hp = 100
        self._alive = True
        __parent__path = Path(__file__).parents[1]
        self.__player__path = __parent__path/'gamecode'/'res'/'airforce5.png'
        self._image = pygame.image.load(self.__player__path)
        original_width = self._image.get_rect().width
        original_height = self._image.get_rect().height
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self._image = pygame.transform.smoothscale(self._image, (new_width, new_height))
        self._center = self._x + self._image.get_rect().w/2,self._y + self._image.get_rect().h/2
        self._radius = 0.3*math.hypot(self._image.get_rect().w,self._image.get_rect().h)

        if xy is None:
            self._x = (self._playground[0] - self._image.get_rect().w)/2
            self._y = 3*self._playground[1]/4
        else:
            self._x = xy[0]
            self._y = xy[1]
        self._objectBound = (10,self._playground[0] - (self._image.get_rect().w + 10),10,self._playground[1] - (self._image.get_rect().h + 10))

    def update(self):
        GameObject.update(self)
        self._center = self._x + self._image.get_rect().w/2,self._y + self._image.get_rect().h/2

    def collide(self, other):
        dx = (self._center[0] - other._center[0])
        dy = (self._center[1] - other._center[1])
        distance = math.hypot(dx, dy)
        return distance < (self._radius + other._radius)

    def collision_detect(self, enemies):
        if not self._alive:
            return
        for enemy in enemies:
            if self.collide(enemy) and enemy._available:
                self._hp -= 10
                enemy._collided = True
                enemy._available = False
                if self._hp <= 0:
                    self._alive = False
                    self._available = False



    #def collision_detect(self,enemies):
        #for m in enemies:
            #self._hp -= 10
            #self._collided = True
            #m.hp = -1
            #m.collided = True
            #m.available = False
