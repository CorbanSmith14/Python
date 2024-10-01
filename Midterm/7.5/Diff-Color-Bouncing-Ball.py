import pygame, sys

pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Bouncing Ball Animation')

WHITE = (255, 255, 255)
ballRadius1 = 20
ballRadius2 = 15
maxRadius1 = 40  # Maximum allowed radius for the first ball
maxRadius2 = 30  # Maximum allowed radius for the second ball
ballX1 = 200  # starting horizontal position for the first ball
ballY1 = 150  # starting vertical position for the first ball
speedX1 = 5  # speed of the first ball's horizontal movement
direction1 = 'right'  # direction of the first ball
colorIndex1 = 0  # index to track the current color of the first ball

ballX2 = 100  # starting horizontal position for the second ball
ballY2 = 50  # starting vertical position for the second ball
speedX2 = 3  # speed of the second ball's horizontal movement
direction2 = 'right'  # direction of the second ball
colorIndex2 = 0  # index to track the current color of the second ball

# List of predefined colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 0)]

while True:
    DISPLAYSURF.fill(WHITE)

    # Update position and direction for the first ball
    if direction1 == 'right':
        ballX1 += speedX1
        if ballX1 >= 400 - ballRadius1:
            direction1 = 'left'
            ballRadius1 = min(ballRadius1 + 5, maxRadius1)
            colorIndex1 = (colorIndex1 + 1) % len(colors)
    elif direction1 == 'left':
        ballX1 -= speedX1
        if ballX1 <= ballRadius1:
            direction1 = 'right'
            ballRadius1 = min(ballRadius1 + 5, maxRadius1)
            colorIndex1 = (colorIndex1 + 1) % len(colors)

    # Update position and direction for the second ball
    if direction2 == 'right':
        ballX2 += speedX2
        if ballX2 >= 400 - ballRadius2:
            direction2 = 'left'
            ballRadius2 = min(ballRadius2 + 3, maxRadius2)
            colorIndex2 = (colorIndex2 + 1) % len(colors)
    elif direction2 == 'left':
        ballX2 -= speedX2
        if ballX2 <= ballRadius2:
            direction2 = 'right'
            ballRadius2 = min(ballRadius2 + 3, maxRadius2)
            colorIndex2 = (colorIndex2 + 1) % len(colors)

    # Check if the first ball has reached maxRadius and reset to original size
    if ballRadius1 == maxRadius1:
        ballRadius1 = 20

    # Check if the second ball has reached maxRadius and reset to original size
    if ballRadius2 == maxRadius2:
        ballRadius2 = 15

    pygame.draw.circle(DISPLAYSURF, colors[colorIndex1], (ballX1, ballY1), ballRadius1)
    pygame.draw.circle(DISPLAYSURF, colors[colorIndex2], (ballX2, ballY2), ballRadius2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
