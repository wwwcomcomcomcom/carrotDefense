import pygame


def loadImage(sprite) -> pygame.Surface:
    return loadImageByData(sprite["imagePath"], sprite["uv"], sprite["size"])


def loadImageByData(imagePath: str, uv: tuple, size: tuple, scale=4) -> pygame.Surface:
    image = pygame.image.load(imagePath)
    rect = pygame.Rect(uv, size)
    return pygame.transform.scale(
        image.subsurface(rect), (size[0] * scale, size[1] * scale)
    )


def cutImageByUv(
    image: pygame.Surface, uv: tuple, size: tuple, scale=4
) -> pygame.Surface:
    rect = pygame.Rect(uv, size)
    return pygame.transform.scale(
        image.subsurface(rect), (size[0] * scale, size[1] * scale)
    )
