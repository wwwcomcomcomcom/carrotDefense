import pygame


class AABB:
    x: float
    y: float
    width: float
    height: float

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def fromVector(cls, vector: pygame.math.Vector2, width, height):
        return cls(vector.x, vector.y, width, height)

    @classmethod
    def fromSurface(cls, x, y, surface: pygame.Surface):
        return cls(x, y, surface.get_width(), surface.get_height())

    @classmethod
    def fromRect(cls, rect: pygame.Rect):
        return cls(rect.x, rect.y, rect.width, rect.height)

    def _getAbsMin(self, a, b):
        if abs(a) < abs(b):
            return a
        else:
            return b

    def feedbackCollision(self, other):
        AminX = self.x
        AminY = self.y
        AmaxX = self.x + self.width
        AmaxY = self.y + self.height
        BminX = other.x
        BminY = other.y
        BmaxX = other.x + other.width
        BmaxY = other.y + other.height

        result = pygame.math.Vector2(0, 0)

        # 충돌 여부 확인
        if AmaxX > BminX and AminX < BmaxX and AmaxY > BminY and AminY < BmaxY:
            # 각 방향으로의 충돌 오프셋 계산
            offsetX1 = BminX - AmaxX  # 왼쪽 충돌
            offsetX2 = BmaxX - AminX  # 오른쪽 충돌
            offsetY1 = BminY - AmaxY  # 위쪽 충돌
            offsetY2 = BmaxY - AminY  # 아래쪽 충돌

            # 가장 작은 오프셋을 선택
            offsets = [offsetX1, offsetX2, offsetY1, offsetY2]
            absOffsets = list(map(abs, offsets))
            minOffset = min(absOffsets)
            minIndex = absOffsets.index(minOffset)

            # X 또는 Y 축에서 벽을 넘지 않도록 피드백 설정
            if minIndex == 0 or minIndex == 1:
                result.x = offsets[minIndex]
            else:
                result.y = offsets[minIndex]

            # 피드백을 조금 더 크게 만들어 벽에서 충분히 떨어지도록 함
            # result *= 1.1  # 피드백에 약간의 여유를 둠

        return result
