import pygame
from object.objectPool import ObjectPool
from tile.tile import TileMap


class Spawner:
    objectPool: ObjectPool
    world: TileMap

    def __init__(self, objectPool: ObjectPool, world: TileMap):
        self.objectPool = objectPool
        self.world = world

    def spawnRandom(self):

        pass

    # def getLightLevel(self,x,y):
    #     self.objectPoolget
