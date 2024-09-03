import pygame
from globalModule import windowHalfWidth, windowHalfHeight


class GameObject:
    x: float
    y: float
    sprite: pygame.Surface

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def getVecotor(self):
        return pygame.math.Vector2(self.x, self.y)

    def setPostion(self, x, y):
        self.x = x
        self.y = y

    def setPositionWithVector(self, vector):
        self.x = vector.x
        self.y = vector.y

    def getTexture(self):
        return self.sprite

    def render(self, screen: pygame.Surface):
        # TODO: fix postion
        screen.blit(self.sprite, (self.x, self.y))
