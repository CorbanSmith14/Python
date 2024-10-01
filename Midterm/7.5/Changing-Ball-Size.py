import pygame, sys

pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Bouncing Ball Animation')

WHITE = (255, 255, 255)
ballRadius = 20
maxRadius = 40  # Maximum allowed radius
ballX = 200  # starting horizontal position
ballY = 150  # starting vertical position
speedX = 5  # speed of ball's horizontal movement
direction = 'right'  # ball's starting direction

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        ballX += speedX
        if ballX >= 400 - ballRadius:  # 400 is window's width
            direction = 'left'
            ballRadius = min(ballRadius + 5, maxRadius)  # Increase radius, but not beyond maxRadius
    elif direction == 'left':
        ballX -= speedX
        if ballX <= ballRadius:
            direction = 'right'
            ballRadius = min(ballRadius + 5, maxRadius)  # Increase radius, but not beyond maxRadius

    # Check if the ball has reached maxRadius and reset to original size
    if ballRadius == maxRadius:
        ballRadius = 20

    pygame.draw.circle(DISPLAYSURF, (0, 0, 255), (ballX, ballY), ballRadius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
