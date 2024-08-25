import json
import pygame
from imageLoader import loadImage


class Pallete:

    def __init__(self):
        with open("tile/tileData.json", "r") as file:
            self.tileData = json.load(file)

        for tileKey, tile in self.tileData.items():
            tile["image"] = loadImage(tile)
            print(f"Loaded tile {tileKey}")

    def get_tile(self, tile_name: str) -> pygame.Surface:
        return self.tileData[tile_name]["image"]
