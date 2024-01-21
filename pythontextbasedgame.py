import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (150, 150, 150)  # Background color
GRID_COLOR = (50, 50, 50)   # Grid color
GRID_SIZE = 40              # Size of each grid square

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Builder Game v0.01")

# Game variables
resources = 100
buildings = []

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle building placement here
        # For example, on mouse click, place a new building
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Add logic to place buildings and deduct resources

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the grid
    draw_grid()

    # Draw buildings
    for building in buildings:
        # Draw each building as a rectangle or use an image
        pygame.draw.rect(screen, (0, 0, 255), (building['x'], building['y'], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

