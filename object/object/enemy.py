import pygame
import json
from globalModule import windowHalfHeight, windowHalfWidth
from object.gameObject import GameObject
from object.animation import Animation

# class Behavior:


class Enemy(GameObject):
    target: GameObject

    def setTarget(self, target: GameObject):
        self.target = target


class Slime(GameObject):
    def __init__(self, x, y):
        slimeConfig = None
        with open("object\\object\\slimeConfig.json", "r") as file:
            slimeConfig = json.load(file)
        self.x = x
        self.y = y
        self.animationState = "default"
        self.animations = Animation.listFromJson(
            slimeConfig["animations"], pygame.image.load(slimeConfig["sprite"])
        )

    def render(self, screen: pygame.Surface, x, y):
        screen.blit(
            self.getCurrentSpirite(),
            (-x - 32 + windowHalfWidth + self.x, -y - 32 + windowHalfHeight + self.y),
        )

    def getCurrentSpirite(self):
        return self.animations[self.animationState].getFrame()
