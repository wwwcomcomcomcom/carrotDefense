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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    player_movement = pygame.math.Vector2(0, 0)
    if keys[pygame.K_LEFT]:
        player_movement.x = -player.speed
    if keys[pygame.K_RIGHT]:
        player_movement.x = player.speed
    if keys[pygame.K_UP]:
        player_movement.y = -player.speed
    if keys[pygame.K_DOWN]:
        player_movement.y = player.speed

    player.x += player_movement.x
    player.y += player_movement.y

    # Update game logic
    tileMap.render(window, player.x, player.y)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
