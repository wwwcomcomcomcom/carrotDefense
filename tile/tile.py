import json
import pygame
from .pallete import Pallete
from typing import List


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

    tiles: List[List[Tile]]

    screen: pygame.Surface

    pallete: Pallete

    def __init__(self, pallete: Pallete):
        mapData = None
        self.tiles = []
        with open("save/town.json", "r") as file:
            mapData = json.load(file)

        for layer, tiles in mapData["layers"].items():
            for y in range(mapData["height"]):
                self.tiles.append(
                    [
                        Tile(
                            x, y, mapData["tile"][str(tiles[x + y * mapData["width"]])]
                        )
                        for x in range(mapData["width"])
                    ]
                )
        self.screen = pygame.Surface((64 * 100, 64 * 100))
        self.pallete = pallete

        for row in self.tiles:
            for tile in row:
                self.screen.blit(
                    pallete.get_tile(tile.tile), (tile.x * 64, tile.y * 64)
                )

    def add_tile(self, x: int, y: int, tile: str):
        self.tiles[x][y] = Tile(x, y, tile)

    def render(self, window: pygame.Surface, x, y):
        window.blit(self.screen, [-x + 960 - 32, -y + 540 - 32])
