import pygame
import json
from globalModule import windowHalfHeight, windowHalfWidth
from object.gameObject import GameObject
from object.animation import Animation
from player import Player
import utils.vectors as VectorUtils


class Enemy(GameObject):
    target: GameObject

    def setTarget(self, target: GameObject):
        self.target = target


class Slime(GameObject):
    target: GameObject

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
        self.target = Player()

    def render(self, screen: pygame.Surface, x, y):
        super().renderSprite(self.getCurrentSpirite(), screen, x, y)

    def update(self):
        self.addVector(
            VectorUtils.moveVector(self.getVecotor(), self.target.getVecotor()) * 300
        )

    def getCurrentSpirite(self):
        return self.animations[self.animationState].getFrame()
