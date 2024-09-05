import pygame
from tile.tile import Tile, TownTileMap
from tile.pallete import Pallete
from player import Player
from globalModule import windowWidth, windowHeight
from object.object.house import House1
from object.object.enemy import Slime

# Initialize Pygame
pygame.init()


window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("My Game")

pallete = Pallete()
tileMap = TownTileMap(pallete)
player = Player(tileMap)
clock = pygame.time.Clock()

house = House1()
slime = Slime(3000, 3000)
# Game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    # Update game logic
    tileMap.render(window, player.x, player.y)
    house.render(window, player.x, player.y)
    slime.render(window, player.x, player.y)
    player.render(window)

    # Update the display
    pygame.display.flip()

    clock.tick(100)

# Quit Pygame
pygame.quit()
