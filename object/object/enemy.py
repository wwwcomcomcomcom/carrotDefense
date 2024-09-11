import pygame
import json
from globalModule import windowHalfHeight, windowHalfWidth
from object.gameObject import GameObject
from object.animation import Animation
from player import Player
import utils.vectors as VectorUtils
import utils.collision as CollisionUtils
from utils.aabb import AABB
from tile.tile import TileMap


class Enemy(GameObject):
    target: GameObject

    def setTarget(self, target: GameObject):
        self.target = target


class Slime(GameObject):
    target: GameObject
    world: TileMap

    def __init__(self, world: TileMap, x, y):
        self.world = world
        self.x = float(x)
        self.y = float(y)
        slimeConfig = None
        with open("object\\object\\slimeConfig.json", "r") as file:
            slimeConfig = json.load(file)
        self.animationState = "default"
        self.animations = Animation.listFromJson(
            slimeConfig["animations"], pygame.image.load(slimeConfig["sprite"])
        )
        self.target = Player()

    def render(self, screen: pygame.Surface, x, y):
        super().renderSprite(self.getCurrentSpirite(), screen, x, y)

    def update(self):
        movement = (
            VectorUtils.moveVector(self.getVecotor(), self.target.getVecotor()) * 4
        )
        targetPosition = self.getVecotor() + movement
        steppingTiles = self.getSteppingTiles(targetPosition)
        steppingTiles = sorted(
            steppingTiles, key=lambda x: targetPosition.distance_to(x)
        )

        index = 0  # 인덱스 변수 추가

        for position in steppingTiles:
            # collideRect = CollisionUtils.getCollideRectWithSize(
            #     self.x + 32, self.y + 32, 64, 64
            # )
            aabb = AABB(self.x, self.y, 64, 64)
            tile = self.world.getTile(position[0], position[1])
            if self.world.pallete.isStepable(tile.tile) == True:
                continue
            else:
                # feedback = Utils.feedbackCollision(
                #     collideRect, tile.getCollideRect()
                # )
                feedback = aabb.feedbackCollision(AABB.fromRect(tile.getCollideRect()))
                targetPosition += feedback
                print(targetPosition)

        self.setVector(targetPosition)

    def getCurrentSpirite(self):
        return self.animations[self.animationState].getFrame()
