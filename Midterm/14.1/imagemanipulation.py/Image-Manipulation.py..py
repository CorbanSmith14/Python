import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
image = pygame.image.load('cat.png')
x, y = 400, 300
angle = 0  # Initial rotation angle
scale_factor = 1.0  # Initial scale factor

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Rotate the image by 45 degrees each time 'R' key is pressed
                angle = (angle + 45) % 360
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                # Increase image size by 20% each time '+' key is pressed
                scale_factor += 0.2
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                # Decrease image size by 20% each time '-' key is pressed
                scale_factor -= 0.2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # Clear the screen
    screen.fill((255, 255, 255))

    # Rotate and scale the image
    rotated_image = pygame.transform.rotate(image, angle)
    scaled_image = pygame.transform.scale(rotated_image, (int(image.get_width() * scale_factor),
                                                          int(image.get_height() * scale_factor)))

    # Blit the scaled and rotated image onto the screen
    screen.blit(scaled_image, (x, y))

    pygame.display.update()

    # Limit the loop to 60 frames per second
    clock.tick(60)
