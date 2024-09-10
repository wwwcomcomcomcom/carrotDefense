import pygame
from object.gameObject import GameObject


class MoveBehavior:
    nodes: list[pygame.math.Vector2]

    def __init__(self, nodes: list[pygame.math.Vector2]):
        self.nodes = nodes
