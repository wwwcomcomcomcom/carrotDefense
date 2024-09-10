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

    def getSteppingTiles(self, origin: tuple[int, int]):
        return [
            origin,
            (origin[0] + 1, origin[1]),
            (origin[0], origin[1] + 1),
            (origin[0] + 1, origin[1] + 1),
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
