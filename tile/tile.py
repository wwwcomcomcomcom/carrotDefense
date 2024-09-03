import json
import pygame
from .pallete import Pallete
from typing import List
from globalModule import windowHalfHeight, windowHalfWidth


class Tile:
    # Readonly
    x: int
    y: int
    tile: str
    state: dict

    def __init__(self, x: int, y: int, tile: str, state: dict = {}):
        self.x = x
        self.y = y
        self.tile = tile

    @classmethod
    def fromJson(cls, x: int, y: int, data: dict):
        return cls(x, y, data["tile"], data["state"])

    def getTexture(self, pallete: Pallete):
        return pallete.getTile(self.tile)

    def stack(self, tile):
        self.tile = StackedTile(self.x, self.y, [self, tile])


class StackedTile(Tile):
    # Readonly
    x: int
    y: int

    tile: str
    state: dict
    layers: List[Tile]

    def __init__(self, x: int, y: int, layers: List[Tile], state: dict = {}):
        self.x = x
        self.y = y
        self.tile = "stacked"
        self.layers = layers
        self.state = state

    # stacked -> tile 만 가능
    # stacked -> stacked 불가능
    @classmethod
    def fromJson(cls, x: int, y: int, data: dict):
        layers = [Tile.fromJson(x, y, tileData) for tileData in data["layers"]]
        return cls(x, y, layers)

    def getTexture(self, pallete: Pallete):
        result = pygame.Surface(64, 64)
        for tile in self.tiles:
            result.blit(pallete.getTile(tile), (0, 0))
        return pallete.getTile(self.tiles)

    def stack(self, tile):
        self.layers.append(tile)
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

    def __init__(self, pallete: Pallete, mapFilePath: str):
        self.tiles = []
        with open(mapFilePath, "r") as file:
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
        window.blit(
            self.screen, [-x + windowHalfWidth - 32, -y + windowHalfHeight - 32]
        )

    def getTile(self, x: int, y: int):
        return self.tiles[x][y]

    def renderTile(self, x, y, tile):
        self.screen.blit(self.pallete.getTile(tile), (x * 64, y * 64))


class TownTileMap(TileMap):

    tiles: List[List[Tile]]

    screen: pygame.Surface

    pallete: Pallete

    def __init__(self, pallete: Pallete):
        super().__init__(pallete, "save/town.json")

    def addTile(self, x: int, y: int, tile: str):
        self.tiles[x][y] = Tile(x, y, tile)

    def setTile(self, x: int, y: int, tile: Tile):
        self.tiles[x][y] = tile

    def setTileWithName(self, x: int, y: int, tile: str):
        self.tiles[x][y] = Tile(x, y, tile)

    def render(self, window: pygame.Surface, x, y):
        window.blit(self.screen, [-x + 960 - 32, -y + 540 - 32])
