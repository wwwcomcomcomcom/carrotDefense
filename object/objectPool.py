import pygame
from typing import List
from object.gameObject import GameObject
from tile.tile import TileMap
from singleton_decorator import singleton


@singleton
class ObjectPool:
    objects: List[GameObject]
    world: TileMap

    def __init__(self, world: TileMap):
        self.objects = []
        self.world = world

    def addObject(self, obj: GameObject):
        self.objects.append(obj)

    def getObject(self, index: int):
        return self.objects[index]

    def removeObject(self, obj: GameObject):
        self.objects.remove(obj)

    def removeObjectByIndex(self, index: int):
        self.objects.pop(index)

    def getObjectsInRange(self, x, y, range):
        objectsInRange = []
        for obj in self.objects:
            if obj.getVecotor().distance_to(pygame.math.Vector2(x, y)) < range:
                objectsInRange.append(obj)
        return objectsInRange

    def render(self, screen: pygame.Surface, x, y):
        for obj in self.objects:
            obj.render(screen, x, y)

    def update(self):
        for obj in self.objects:
            obj.update()
