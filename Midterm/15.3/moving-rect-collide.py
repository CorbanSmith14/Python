import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision Detection with Pygame")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up rectangles
static_rect_size = (50, 50)
static_rect_position = (width // 2 - static_rect_size[0] // 2, height // 2 - static_rect_size[1] // 2)
static_rect = pygame.Rect(static_rect_position, static_rect_size)

moving_rect_size = (50, 50)
moving_rect_position = (random.randint(0, width - moving_rect_size[0]), random.randint(0, height - moving_rect_size[1]))
moving_rect = pygame.Rect(moving_rect_position, moving_rect_size)

# Set up movement speed
speed = 5

# Load beep sound
beep_sound = pygame.mixer.Sound("beep.wav")  # Make sure to replace "beep.wav" with the actual path to your sound file

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the moving rectangle
    if keys[pygame.K_LEFT] and moving_rect.left > 0:
        moving_rect.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT] and moving_rect.right < width:
        moving_rect.move_ip(speed, 0)
    if keys[pygame.K_UP] and moving_rect.top > 0:
        moving_rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN] and moving_rect.bottom < height:
        moving_rect.move_ip(0, speed)

    # Check for collision
    if moving_rect.colliderect(static_rect):
        beep_sound.play()

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, red, static_rect)
    pygame.draw.rect(screen, red, moving_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
