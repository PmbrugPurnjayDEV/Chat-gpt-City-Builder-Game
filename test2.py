import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 40
BUILDING_SIZE = 35
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GAME_NAME = "MetroGrid Constructor"
VERSION = "Alpha 1.0.0"

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"{GAME_NAME} - {VERSION}")

# Game variables
buildings = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Calculate the grid cell coordinates
            x, y = event.pos
            grid_x = x // GRID_SIZE * GRID_SIZE
            grid_y = y // GRID_SIZE * GRID_SIZE

            # Center the building in the grid cell
            building_x = grid_x + (GRID_SIZE - BUILDING_SIZE) // 2
            building_y = grid_y + (GRID_SIZE - BUILDING_SIZE) // 2

            buildings.append((building_x, building_y))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    # Draw the buildings
    for building in buildings:
        pygame.draw.rect(screen, BLUE, (building[0], building[1], BUILDING_SIZE, BUILDING_SIZE))

    # Update the display
    pygame.display.flip()

pygame.quit()
