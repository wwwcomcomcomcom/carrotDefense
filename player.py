import pygame
import json
from tile.tile import TileMap
from object.gameObject import GameObject
from object.animation import Animation
from singleton_decorator import singleton
import utils.collision as CollisionUtils


@singleton
class Player(GameObject):
    x: float
    y: float

    animationState: str
    animations: dict[str, Animation]

    speed: float
    size: float
    world: TileMap

    lastDirection: str

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

        self.animationState = "idleDown"
        self.lastDirection = "Down"
        self.animations = Animation.listFromJson(
            playerConfig["animations"], pygame.image.load(playerConfig["sprite"])
        )

    def move(self):
        keys = pygame.key.get_pressed()
        playerMovement = pygame.math.Vector2(0, 0)
        self.animationState = "idle" + self.lastDirection
        if keys[pygame.K_LEFT]:
            playerMovement.x = -self.speed
            self.animationState = "walkLeft"
            self.lastDirection = "Left"
        if keys[pygame.K_RIGHT]:
            playerMovement.x = self.speed
            self.animationState = "walkRight"
            self.lastDirection = "Right"
        if keys[pygame.K_UP]:
            playerMovement.y = -self.speed
            self.animationState = "walkUp"
            self.lastDirection = "Up"
        if keys[pygame.K_DOWN]:
            playerMovement.y = self.speed
            self.animationState = "walkDown"
            self.lastDirection = "Down"

        targetPosition = self.getVecotor() + playerMovement
        for position in self.getSteppingTiles(
            [int(targetPosition.x) // 64, int(targetPosition.y) // 64]
        ):
            collideRect = CollisionUtils.getCollideRectWithSize(
                targetPosition.x + 32, targetPosition.y + 32, 64, 64
            )
            tile = self.world.tiles[position[1]][position[0]]
            if self.world.pallete.isStepable(tile.tile) == True:
                continue
            else:
                targetPosition += CollisionUtils.feedbackCollision(
                    collideRect, tile.getCollideRect()
                )
        self.setVector(targetPosition)
        # tileX = (self.x + playerMovement.x) / 64
        # tileY = (self.y + playerMovement.y) / 64
        # if self.world.tiles[round(tileY)][round(tileX)].tile == "water":
        #     return

        # self.x += playerMovement.x
        # self.y += playerMovement.y

    def getCurrentSprite(self):
        return self.animations[self.animationState].getFrame()

    def render(self, screen: pygame.Surface):
        originSize = self.getCurrentSprite().get_size()
        screen.blit(
            pygame.transform.scale(
                self.getCurrentSprite(),
                (int(originSize[0] * self.size), int(originSize[1] * self.size)),
            ),
            [960 - 32, 540 - 32],
        )
