import math

@property
def x(self):
    return  self._x
@property
def y(self):
    return  self._y
@property
def hp(self):
    return  self._hp

@y.setter
def x(self,value):
    self._x = value
@y.setter
def y(self,value):
    self._y = value
@hp.setter
def hp(self,value):
    self._hp = value
@property
def available(self):
    return self._available

@available.setter
def available(self, value):
    self._available = value


class GameObject:
    def __init__(self,playground=None):
        if playground is None:
            self._playground = [1200,900]
        else:
            self._playground = playground

        self._objectBound = (0,self._playground[0],0,self._playground[1])
        self._changeX = 0
        self._changeY = 0
        self._x = 0
        self._y = 0
        self._moveScale = 1
        self._hp = 1
        self._image = None
        self._available = True
        self._center = None
        self._radius = None
        self._collided = False

    def __del__(self):
        print(self.__class__.__name__,"is being automatically destroyed. Goodbye!")

    def to_the_left(self):
        self._changeX = -self._moveScale
    def to_the_right(self):
        self._changeX = self._moveScale
    def to_the_bottom(self):
        self._changeY = self._moveScale
    def to_the_top(self):
        self._changeY = -self._moveScale
    def stop_x(self):
        self._changeX = 0
    def stop_y(self):
        self._changeY = 0

    def update(self):
        self._x += self._changeX
        self._y += self._changeY
        if self._x > self._objectBound[1]:
           self._x = self._objectBound[1]
        if self._x < self._objectBound[0]:
           self._x = self._objectBound[0]
        if self._y > self._objectBound[3]:
           self._y = self._objectBound[3]
        if self._y < self._objectBound[2]:
           self._y = self._objectBound[2]
    def _collided_(self,it):
        distance = math.hypot(self._center[0] - it.center[0],self._center[1] - it.center[1])
        if distance < self._radius + it.raduis:
            return True
        else:
            return False