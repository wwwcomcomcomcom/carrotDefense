import pygame
import json


class GameObject:
    x: float
    y: float
    sprite: pygame.Surface
    state: str
    animation: dict
    animatedTime: int
    animationFrame: int

    def __init__(self, x, y, sprite, state, animation, animatedTime, animationFrame):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.state = state
        self.animation = animation
        self.animatedTime = animatedTime
        self.animationFrame = animationFrame

    @classmethod
    def from_json(filePath: str):
        data = None
        with open(filePath, "r") as file:
            data = json.load(file)
        return Object(
            float(data["x"]),
            float(data["y"]),
            pygame.image.load(data["sprite"]),
            "",
            data["animation"],
            pygame.time.get_ticks(),
            0,
        )
