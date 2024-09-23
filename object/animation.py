import pygame
from typing import List, Dict
from utils.imageLoader import cutImageByUv


class Animation:
    frames: List[pygame.Surface]
    # Smaller is slower
    speed: float
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
        self.frames = []
        for uvData in data["frames"]:
            uv = uvData["uv"]
            size = uvData["size"]
            self.frames.append(cutImageByUv(sprite, uv, size))

    @classmethod
    def listFromJson(cls, data: dict, sprite: pygame.Surface) -> Dict[str, any]:
        result = {}
        for key, animation in data.items():
            result[key] = cls(animation, sprite)
        return result

    # also update frames
    def getFrame(self) -> pygame.Surface:
        if pygame.time.get_ticks() - self.animatedTime * self.speed > 100:
            self.animatedTime = pygame.time.get_ticks()
            self.animationFrame += 1
            if self.animationFrame >= len(self.frames):
                self.animationFrame = 0
        return self.frames[self.animationFrame]
