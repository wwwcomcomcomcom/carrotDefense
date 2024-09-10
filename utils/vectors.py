import pygame


# 방향 벡터를 반환합니다.
def moveVector(fromVec: pygame.Vector2, toVec: pygame.Vector2) -> pygame.math.Vector2:
    targetVector = pygame.Vector2(toVec.x - fromVec.x, toVec.y - fromVec.y)
    if targetVector.length() == 0:
        return targetVector
    return targetVector.normalize()
