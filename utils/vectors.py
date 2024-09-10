import pygame


# 방향 벡터를 반환합니다.
def moveVector(fromVec: pygame.Vector2, toVec: pygame.Vector2) -> pygame.math.Vector2:

    distance = fromVec.distance_to(toVec)
    targetVector = pygame.math.Vector2(toVec.x - fromVec.x, toVec.y - fromVec.y)
    return targetVector / distance / 64
