import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Chase")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Circle properties
circle_radius = 20
target_radius = 30

# Create a target circle at a random position
target_pos = [random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius)]

# Create a moving circle at the bottom left corner
circle_pos = [circle_radius, height - circle_radius]

# Set the speed of the moving circle
speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the circle towards the target
    angle = math.atan2(target_pos[1] - circle_pos[1], target_pos[0] - circle_pos[0])
    circle_pos[0] += speed * math.cos(angle)
    circle_pos[1] += speed * math.sin(angle)

    # Check if the moving circle reaches the target
    distance = math.sqrt((circle_pos[0] - target_pos[0])**2 + (circle_pos[1] - target_pos[1])**2)
    if distance < target_radius + circle_radius:
        target_pos = [random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius)]

    # Clear the screen
    screen.fill(white)

    # Draw the target circle
    pygame.draw.circle(screen, red, (int(target_pos[0]), int(target_pos[1])), target_radius)

    # Draw the moving circle
    pygame.draw.circle(screen, black, (int(circle_pos[0]), int(circle_pos[1])), circle_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
