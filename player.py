import pygame
import json
import time
from imageLoader import loadImage, cutImageByUv
from tile.tile import TileMap


class Player:
    x: float
    y: float
    speed: float
    size: float
    state: str

    sprite: pygame.Surface
    animation: dict
    animatedTime: int
    animationFrame: int

    world: TileMap

    def __init__(self, world: TileMap):
        playerConfig = None
        with open("playerConfig.json", "r") as file:
            playerConfig = json.load(file)
        playerData = None
        with open("save/player.json", "r") as file:
            playerData = json.load(file)
        self.x = playerData["x"]
        self.y = playerData["y"]

        self.speed = playerConfig["speed"]
        self.size = float(playerConfig["size"])
        self.sprite = pygame.image.load(playerConfig["sprite"]["imagePath"])
        self.animation = playerConfig["animation"]
        self.animatedTime = pygame.time.get_ticks()
        self.animationFrame = 0
        self.world = world

        loadImage(playerConfig["sprite"])
        self.state = "idle"

    def vector(self):
        return pygame.math.Vector2(self.x, self.y)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        player_movement = pygame.math.Vector2(0, 0)
        if keys[pygame.K_LEFT]:
            player_movement.x = -self.speed
        if keys[pygame.K_RIGHT]:
            player_movement.x = self.speed
        if keys[pygame.K_UP]:
            player_movement.y = -self.speed
        if keys[pygame.K_DOWN]:
            player_movement.y = self.speed

        tileX = (self.x + player_movement.x) / 64
        tileY = (self.y + player_movement.y) / 64
        if self.world.tiles[round(tileY)][round(tileX)].tile == "water":
            print(tileX, tileY)
            return

        self.x += player_movement.x
        self.y += player_movement.y

    def getCurrentSprite(self):
        if len(self.animation[self.state]["frames"]) == 1:
            uv = self.animation[self.state]["frames"][0]["uv"]
            size = self.animation[self.state]["frames"][0]["size"]
            return cutImageByUv(self.sprite, uv, size, self.size * 4)
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

    def render(self, screen: pygame.Surface):
        screen.blit(self.getCurrentSprite(), [960 - 32, 540 - 32])
