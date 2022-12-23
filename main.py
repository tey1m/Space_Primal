import pygame
import Player as player

# Window dimensions
WIDTH = 1920
HEIGHT = 1080

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Primal Survival Pixel")

grass = pygame.image.load("images/player.png")

# Create player instance
player = player.Player(WIDTH, HEIGHT, WIDTH // 2, HEIGHT // 2, 0, 0, 0, 0, 0.46)


# Game loop variables
running = True
pressed_key = None
released_key = None

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressed_key = event.key
        if event.type == pygame.KEYUP:
            released_key = event.key
            if pressed_key == released_key:
                released_key = None
                pressed_key = None

    # Handle player movement
    player.move(pressed_key)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw game objects
    player.map.draw_map(player.camera_x, player.camera_y, player.player_x, player.player_y)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
