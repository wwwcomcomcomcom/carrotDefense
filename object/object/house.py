import pygame
from object.gameObject import GameObject
from globalModule import windowHalfHeight, windowHalfWidth
from imageLoader import loadImageByData


class House1(GameObject):

    def __init__(self):
        image = loadImageByData(
            "assets\\map\\Buildings\\Purple\\PurpleChapels.png", (0, 16), (16, 16), 8
        )
        super().__init__(50 * 64, 50 * 64, image)

    def render(self, screen: pygame.Surface, x, y):
        screen.blit(
            self.sprite,
            (-x - 32 + windowHalfWidth + self.x, -y - 32 + windowHalfHeight + self.y),
        )

    def nextLevel(self):
        return House2()


class House2(GameObject):

    def __init__(self):
        image = loadImageByData(
            "assets\\map\\Buildings\\Purple\\PurpleKeep.png", (0, 0), (32, 32), 3 / 2
        )
        super().__init__(50 * 64, 50 * 64, image)

    def render(self, screen: pygame.Surface, x, y):
        screen.blit(
            self.sprite,
            (-x - 32 + windowHalfWidth + self.x, -y - 32 + windowHalfHeight + self.y),
        )
