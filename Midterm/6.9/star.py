import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Three Stars")

# Define colors
orange = (255, 165, 0)
black = (0, 0, 0)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # black background
    screen.fill(black)

    # first star with a black outline
    size = 80
    x1, y1 = width // 4, height // 2
    points1 = []

    for i in range(5):
        outer_x = x1 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).x
        outer_y = y1 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).y

        inner_x = x1 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).x
        inner_y = y1 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).y

        points1.extend([(outer_x, outer_y), (inner_x, inner_y)])

    pygame.draw.polygon(screen, black, points1, 2)  # Draw with a black outline
    pygame.draw.polygon(screen, (255, 255, 255), points1)  # Fill with a white color

    # second star middle star in orange
    x2, y2 = width // 2, height // 2
    points2 = []

    for i in range(5):
        outer_x = x2 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).x
        outer_y = y2 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).y

        inner_x = x2 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).x
        inner_y = y2 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).y

        points2.extend([(outer_x, outer_y), (inner_x, inner_y)])

    pygame.draw.polygon(screen, orange, points2)

    # third star with a black outline
    x3, y3 = 3 * width // 4, height // 2
    points3 = []

    for i in range(5):
        outer_x = x3 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).x
        outer_y = y3 + size * 0.8 * pygame.math.Vector2(1, 0).rotate(i * 360 / 5).y

        inner_x = x3 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).x
        inner_y = y3 + size * 0.4 * pygame.math.Vector2(1, 0).rotate((i + 0.5) * 360 / 5).y

        points3.extend([(outer_x, outer_y), (inner_x, inner_y)])

    pygame.draw.polygon(screen, black, points3, 2)  # Draw with a black outline
    pygame.draw.polygon(screen, (255, 255, 255), points3)  # Fill with a white color

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
