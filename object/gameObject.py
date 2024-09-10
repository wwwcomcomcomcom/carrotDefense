import pygame
from globalModule import windowHalfWidth, windowHalfHeight
from tile.tile import TileMap


class GameObject:
    x: float
    y: float
    sprite: pygame.Surface

    def __init__(self, x, y, sprite=None):
        self.x = x
        self.y = y
        self.sprite = sprite

    def getVecotor(self):
        return pygame.math.Vector2(self.x, self.y)

    def setVector(self, vector):
        self.x = vector.x
        self.y = vector.y

    def addVector(self, vector):
        self.x += vector.x
        self.y += vector.y

    def setPostion(self, x, y):
        self.x = x
        self.y = y

    def setPositionWithVector(self, vector):
        self.x = vector.x
        self.y = vector.y

    def getCurrentSprite(self):
        return self.sprite

    def getTilePosition(self):
        return (int(self.x // 64), int(self.y // 64))

    # @params postion: not tile position
    def getSteppingTiles(self, postion: pygame.math.Vector2):
        origin = postion.copy()
        origin.x = int(origin.x // 64)
        origin.y = int(origin.y // 64)
        return [
            (int(origin.x), int(origin.y)),
            (int(origin.x + 1), int(origin.y)),
            (int(origin.x), int(origin.y + 1)),
            (int(origin.x + 1), int(origin.y + 1)),
            (int(origin.x - 1), int(origin.y)),
            (int(origin.x), int(origin.y - 1)),
            (int(origin.x - 1), int(origin.y - 1)),
            (int(origin.x + 1), int(origin.y - 1)),
        ]

    def render(self, screen: pygame.Surface, x, y):
        sprite = self.getCurrentSprite()
        self._render(sprite, screen, x, y)

    def renderSprite(self, sprite: pygame.Surface, screen: pygame.Surface, x, y):
        screen.blit(
            sprite,
            (
                -x + windowHalfWidth + self.x - sprite.get_width() / 2,
                -y + windowHalfHeight + self.y - sprite.get_height() / 2,
            ),
        )

    def update(self):
        pass
