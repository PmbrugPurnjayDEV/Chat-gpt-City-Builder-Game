import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (150, 150, 150)  # Background color
GRID_COLOR = (50, 50, 50)   # Grid color
GRID_SIZE = 40              # Size of each grid square
RESIDENTIAL_COLOR = (255, 0, 0)  # Color for residential buildings

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Builder Game v0.02")

# Game variables
resources = 100
buildings = []

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

def add_building(x, y):
    # Align the building to the grid
    grid_x = x - (x % GRID_SIZE)
    grid_y = y - (y % GRID_SIZE)
    buildings.append({'x': grid_x, 'y': grid_y, 'type': 'residential'})

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            add_building(mouse_x, mouse_y)

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the grid
    draw_grid()

    # Draw buildings
    for building in buildings:
        if building['type'] == 'residential':
            pygame.draw.rect(screen, RESIDENTIAL_COLOR, (building['x'], building['y'], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
