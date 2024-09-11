import pygame


def getCollideRect(x, y, sprite: pygame.Surface):
    return pygame.Rect(
        x - sprite.get_width() / 2,
        y - sprite.get_height() / 2,
        sprite.get_width(),
        sprite.get_height(),
    )


def getCollideRectWithSize(x, y, width, height):
    return pygame.Rect(
        round(x) - width / 2,
        round(y) - height / 2,
        width,
        height,
    )


def feedbackCollision(obj1: pygame.rect.Rect, obj2: pygame.rect.Rect):
    AminX = obj1.x
    AminY = obj1.y
    AmaxX = obj1.x + obj1.width
    AmaxY = obj1.y + obj1.height
    BminX = obj2.x
    BminY = obj2.y
    BmaxX = obj2.x + obj2.width
    BmaxY = obj2.y + obj2.height

    result = pygame.math.Vector2(0, 0)
    if AmaxX > BminX and AminX < BmaxX and AmaxY > BminY and AminY < BmaxY:
        allOfset = [
            (BminX - AmaxX),
            (BmaxX - AminX),
            (BminY - AmaxY),
            (BmaxY - AminY),
        ]
        absArray = list(map(abs, allOfset))
        minOfset = min(absArray)
        minIndex = absArray.index(minOfset)

        if minIndex == 0:
            result.x = allOfset[0]
        elif minIndex == 1:
            result.x = allOfset[1]
        elif minIndex == 2:
            result.y = allOfset[2]
        elif minIndex == 3:
            result.y = allOfset[3]

    return result
    # if AmaxX > BminX and AminX < BmaxX:
    #     if abs(AmaxX - BminX) < abs(BmaxX - AminX):
    #         Xdiff = AmaxX - BminX
    #     else:
    #         Xdiff = BmaxX - AminX
    # if AmaxY > BminY and AminY < BmaxY:
    #     if abs(AmaxY - BminY) < abs(BmaxY - AminY):
    #         Ydiff = AmaxY - BminY
    #     else:
    #         Ydiff = BmaxY - AminY

    # if Xdiff > Ydiff:
    #     return (0, Ydiff)
    # else:
    #     return (Xdiff, 0)
