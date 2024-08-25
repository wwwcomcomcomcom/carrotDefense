import json
import pygame
from .pallete import Pallete


class Tile:
    x: int
    y: int
    tile: str

    def __init__(self, x: int, y: int, tile: str):
        self.x = x
        self.y = y
        self.tile = tile

    def getTexture(self, pallete: Pallete):
        return pallete.get_tile(self.tile)


# {
#     "name": "Grass",
#     "imagePath": "grass.png",
#     "uv": [0, 0],
#     "size": [16, 16]
#     "image": Surface pygame.image.load("assets/map/Ground/grass.png")
# }


class TileMap:

    tiles: list[Tile]

    screen: pygame.Surface

    pallete: Pallete

    def __init__(self, pallete: Pallete):
        self.tiles = [Tile(i, j, "grass") for j in range(100) for i in range(100)]
        self.screen = pygame.Surface((60 * 100, 60 * 100))
        self.pallete = pallete

        for tile in self.tiles:
            self.screen.blit(pallete.get_tile(tile.tile), (tile.x * 60, tile.y * 60))

    def add_tile(self, x: int, y: int, tile: str):
        self.tiles.append(Tile(x, y, tile))

    def render(self, window: pygame.Surface, x, y):
        window.blit(self.screen, [-x, -y])
        # for tile in self.tiles:
        #     window.blit(self.pallete.get_tile(tile.tile), (tile.x * 60, tile.y * 60))
