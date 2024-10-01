import pygame, sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SPEED = 4  # Increased speed
ZIGZAG_SPAN = 80  # Increased vertical distance before changing direction

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the display and clock
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Horizontal Zigzag Pattern Movement')
fpsClock = pygame.time.Clock()

# Ball's starting position and direction
x, y = WIDTH // 2, 0
dir_x = 1  # Horizontal direction
dir_y = 1  # Vertical direction
initial_x = x
initial_y = y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    x += SPEED * dir_x
    y += SPEED * dir_y

    # Check if the horizontal zigzag span is covered
    if abs(x - initial_x) >= ZIGZAG_SPAN:
        dir_x *= -1  # Reverse horizontal direction
        initial_x = x  # Reset the initial position for the next span

    # Boundary checks to keep the object within the display
    if x < 0:
        x = 0
        dir_x *= -1  # Reverse horizontal direction

    if x > WIDTH:
        x = WIDTH
        dir_x *= -1  # Reverse horizontal direction

    if y < 0:
        y = 0
        dir_y *= -1  # Reverse vertical direction

    if y > HEIGHT:
        y = HEIGHT
        dir_y *= -1  # Reverse vertical direction

    pygame.draw.circle(DISPLAYSURF, RED, (int(x), int(y)), 10)
    pygame.display.flip()
    fpsClock.tick(60)
