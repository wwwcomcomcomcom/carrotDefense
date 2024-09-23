import pygame
from utils.imageLoader import loadImageByData
from player import Player
from globalModule import windowHalfWidth, windowHalfHeight


class GUI:
    tileSelectSprite: pygame.Surface
    screen: pygame.Surface
    player: Player

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.tileSelectSprite = loadImageByData(
            "assets\\ui\\Sprite sheets\\select.png", [0, 0], [64, 64], 1
        )
        self.player = Player()

    def render(self):
        targetPos = [0, 0]
        targetPos[0] = windowHalfWidth - ((self.player.x + 32) % 64)
        targetPos[1] = windowHalfHeight - ((self.player.y + 32) % 64)
        mousePos = list(pygame.mouse.get_pos())
        targetPos[0] += mousePos[0] + 32 - ((mousePos[0] + 32) % 64) - windowHalfWidth
        targetPos[1] += mousePos[1] - (mousePos[1] % 64) - windowHalfHeight + 32
        self.screen.blit(self.tileSelectSprite, targetPos)
