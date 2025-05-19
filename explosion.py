import random

import pygame.image
from pathlib import Path
from gameObject import GameObject




class Explosion(GameObject):

    explosion_effect = []

    def __init__(self, xy=None):
        GameObject.__init__(self)
        if xy is None:
            self._y = -100
            self._x = random.randint(10,self._playground[0] - 100)
        else:
            self._x = xy[0]
            self._y = xy[1]


        if Explosion.explosion_effect:
            pass
        else:

            __parent_path = Path(__file__).parents[1]

            scale_size = (50, 50)

            icon_path = __parent_path/'gamecode'/'res'/'boom1.png'
            img = pygame.image.load(icon_path)
            Explosion.explosion_effect.append(pygame.transform.scale(img, scale_size))
            icon_path = __parent_path/'gamecode'/'res'/'boom2.png'
            img = pygame.image.load(icon_path)
            Explosion.explosion_effect.append(pygame.transform.scale(img, scale_size))
            icon_path = __parent_path/'gamecode'/'res'/'boom3.png'
            img = pygame.image.load(icon_path)
            Explosion.explosion_effect.append(pygame.transform.scale(img, scale_size))
            icon_path = __parent_path/'gamecode'/'res'/'boom2.png'
            img = pygame.image.load(icon_path)
            Explosion.explosion_effect.append(pygame.transform.scale(img, scale_size))


        self.__image_index = 0
        self._image = Explosion.explosion_effect[self.__image_index]
        self.__fps_count = 0

    def update(self):
        self.__fps_count += 1
        if self.__fps_count > 30:
            self.__image_index += 1
            if self.__image_index >= len(Explosion.explosion_effect):
                self._available = False
            else:
                self._image = Explosion.explosion_effect[self.__image_index]
