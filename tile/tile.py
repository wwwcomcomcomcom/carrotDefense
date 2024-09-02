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
        return pallete.getTile(self.tile)

    def stack(self, tile: str):
        self.tile = StackedTile(self.x, self.y, [self.tile, tile])


class StackedTile(Tile):
    x: int
    y: int
    tiles: List[str]

    def __init__(self, x: int, y: int, tiles: List[str]):
        self.x = x
        self.y = y
        self.tiles = tiles

    def getTexture(self, pallete: Pallete):
        result = pygame.Surface(64, 64)
        for tile in self.tiles:
            result.blit(pallete.getTile(tile), (0, 0))
        return pallete.getTile(self.tiles)

    def stack(self, tile: str):
        self.tiles.append(tile)
        return self


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

        for tiles in mapData["layers"]:
            for y in range(mapData["height"]):
                self.tiles.append(
                    [
                        Tile(
                            x, y, mapData["tile"][str(tiles[x + y * mapData["width"]])]
                        )
                        for x in range(mapData["width"])
                    ]
                )
        self.screen = pygame.Surface((64 * mapData["width"], 64 * mapData["height"]))
        self.pallete = pallete

        for row in self.tiles:
            for tile in row:
                self.screen.blit(pallete.getTile(tile.tile), (tile.x * 64, tile.y * 64))

    def addTile(self, x: int, y: int, tile: str):
        self.tiles[x][y] = Tile(x, y, tile)

    def setTile(self, x: int, y: int, tile: Tile):
        self.tiles[x][y] = tile

    def setTileWithName(self, x: int, y: int, tile: str):
        self.tiles[x][y] = Tile(x, y, tile)

    def render(self, window: pygame.Surface, x, y):
        window.blit(self.screen, [-x + 960 - 32, -y + 540 - 32])
