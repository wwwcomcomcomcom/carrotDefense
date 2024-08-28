import pygame
from tile.tile import Tile, TileMap
from tile.pallete import Pallete
from player import Player
from globalModule import windowWidth, windowHeight

# Initialize Pygame
pygame.init()


window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("My Game")

pallete = Pallete()
tileMap = TileMap(pallete)
player = Player(tileMap)
clock = pygame.time.Clock()

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
    player.render(window)

    # Update the display
    pygame.display.flip()

    clock.tick(100)

# Quit Pygame
pygame.quit()
