import pygame

class Obstacle:
    def __init__(self, x, y, width, height, vel_x, color):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self.vel_x = vel_x
        self.passed_player = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def update(self):
        self._x -= self.vel_x

    def draw(self, surface):
        pygame.draw.rect(surface, self._color, [self._x, self._y, self._width, self._height])

    def is_colliding(self, player):
        result = False
        if player.x + player.width >= self.x and player.x <= (self.x + self.width)\
                and player.y + player.height >= self.y and player.y <= self.y + self.height:
            result = True
        return result
