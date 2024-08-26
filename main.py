import pygame
from tile.tile import Tile, TileMap
from tile.pallete import Pallete
from player import Player

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1920
window_height = 1080

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")


player = Player()
pallete = Pallete()
tileMap = TileMap(pallete)

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

# Quit Pygame
pygame.quit()
