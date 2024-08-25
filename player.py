import pygame
import json
import time
from imageLoader import loadImage, cutImageByUv

time.time()


class Player:
    x: float
    y: float
    speed: float
    state: str

    sprite: pygame.Surface

    animation: dict
    # time.time()
    animatedTime: float
    animationFrame: int

    def __init__(self):
        jsonData = None
        with open("playerData.json", "r") as file:
            jsonData = json.load(file)

        self.speed = jsonData["speed"]
        self.sprite = pygame.image.load(jsonData["sprite"]["imagePath"])
        self.animation = jsonData["animation"]
        self.animatedTime = time.time()
        self.animationFrame = 0

        loadImage(jsonData["sprite"])

        self.x = 0
        self.y = 0

        self.state = "idle"

    def vector(self):
        return pygame.math.Vector2(self.x, self.y)

    def getCameraTileRange(self):
        # 1920/2 = 960 1080/2 = 540
        return {
            "start_x": int((self.x + 960) // 60 + 1),
            "end_x": int((self.y - 960) // 60 - 1),
            "start_y": int((self.y + 540) // 60 + 1),
            "end_y": int((self.y - 540) // 60 - 1),
        }

    def getCurrentSprite(self):
        if len(self.animation[self.state]) == 1:
            uv = self.animation[self.state][0]["uv"]
            size = self.animation[self.state][0]["size"]
            return cutImageByUv(self.sprite, uv, size)
        if (
            time.time() - self.animatedTime
            > self.animation[self.state][self.animationFrame]["time"]
        ):
            self.animationFrame += 1
            self.animatedTime = time.time()

        return cutImageByUv(
            self.sprite,
            self.animation[self.state][self.animationFrame]["uv"],
            self.animation[self.state][self.animationFrame]["size"],
        )
