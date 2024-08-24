import json
import pygame


class Tile:
    x: int
    y: int
    tile: str

    def __init__(self, x: int, y: int, tile: str):
        self.x = x
        self.y = y
        self.tile = tile


# {
#     "name": "Grass",
#     "imagePath": "grass.png",
#     "uv": [0, 0],
#     "size": [16, 16]
#     "image": Surface pygame.image.load("assets/map/Ground/grass.png")
# }


class TileLoader:

    def __init__(self):
        with open("tiles/tileData.json", "r") as file:
            self.tileData = json.load(file)

        # tileKey를 Group처럼 사용해서 imageLoad를 최적화 할 수 있음
        for tileKey, tile in self.tileData.items():
            image = pygame.image.load(f"assets/map/Ground/{tile['imagePath']}")
            rect = pygame.Rect(tile["uv"], tile["size"])
            tile["image"] = image.subsurface(rect)

    def get_tile(self, tile_name: str):
        return
