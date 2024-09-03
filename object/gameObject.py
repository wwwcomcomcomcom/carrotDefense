import pygame
from globalModule import windowHalfWidth, windowHalfHeight
from typing import Dict, List, Tuple
from imageLoader import cutImageByUv


class Animation:
    frames: List[pygame.Surface]
    # Bigger is slower
    speed: int
    animatedTime: int
    animationFrame: int

    # "frames": [
    #     {
    #       "uv": [0, 0],
    #       "size": [16, 16]
    #     }
    #   ]
    def __init__(self, data: dict, sprite: pygame.Surface):
        self.speed = data["speed"]
        self.animatedTime = pygame.time.get_ticks()
        self.animationFrame = 0
        for uvData in data["frames"]:
            uv = uvData["uv"]
            size = uvData["size"]
            self.frames.append(cutImageByUv(sprite, uv, size))

    # also update frames
    def getFrame(self) -> pygame.Surface:
        if pygame.time.get_ticks() - self.animatedTime > self.speed:
            self.animatedTime = pygame.time.get_ticks()
            self.animationFrame += 1
            if self.animationFrame >= len(self.frames):
                self.animationFrame = 0
        return self.frames[self.animationFrame]


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
        screen.blit(self.sprite, (self.x, self.y))
