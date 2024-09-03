import pygame
import json
import time
from imageLoader import loadImage, cutImageByUv
from tile.tile import TileMap
from object.gameObject import GameObject
from object.animation import Animation


class Player(GameObject):
    x: float
    y: float

    animationState: str
    animations: dict[str, Animation]

    speed: float
    size: float
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
        self.world = world

        self.animationState = "idle"
        self.animations = Animation.listFromJson(
            playerConfig["animations"], pygame.image.load(playerConfig["sprite"])
        )

    def vector(self):
        return pygame.math.Vector2(self.x, self.y)

    def move(self):
        keys = pygame.key.get_pressed()
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
        return self.animations[self.animationState].getFrame()

    def render(self, screen: pygame.Surface):
        screen.blit(self.getCurrentSprite(), [960 - 32, 540 - 32])
