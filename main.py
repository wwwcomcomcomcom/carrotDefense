import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Load the image
image_path = "./assets/map/Ground/grass.png"
image = pygame.image.load(image_path)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render graphics
    window.blit(
        image, (0, 0)
    )  # Blit the image onto the window surface at position (0, 0)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
