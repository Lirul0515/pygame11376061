from gameObject import GameObject
from pathlib import Path
import pygame




class MyMissile(GameObject):

    def __init__(self,playground,xy,sensitivity = 1,scale_factor = 0.07):
        GameObject.__init__(self,playground)
        __parent_path = Path(__file__).parents[1]
        self.__missile_path = __parent_path/'gamecode'/'res'/'missile3.png'
        self._image = pygame.image.load(self.__missile_path)
        original_width = self._image.get_rect().width
        original_height = self._image.get_rect().height
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self._image = pygame.transform.smoothscale(self._image, (new_width, new_height))
        self._center = self._x + self._image.get_rect().w/2, self._y + self._image.get_rect().w/2
        self._radius = self._image.get_rect().w/2
        self._x = xy[0]
        self._y = xy[1]

        self._objectBound = (0,self._playground[0],-self._image.get_rect().h - 10,self._playground[1])
        self._moveScale = 0.7*sensitivity
        self.to_the_top()

    def update(self):
        self._y += self._changeY
        if self._y < self._objectBound[2]:
            self._available = False
        self._center = self._x + self._image.get_rect().w/2,self._y + self._image.get_rect().w/2
    def collide(self, other):
        dx = self._center[0] - other._center[0]
        dy = self._center[1] - other._center[1]
        distance = (dx**2 + dy**2)**0.5
        return distance < (self._radius + other._radius)

    def collision_detect(self,enemies):
        for m in enemies:
            if self.collided(m):
                self._hp -= 10
                self._collided = True
                self._available = False
                m.hp = -1
                m.collided = True
                m.available = False

