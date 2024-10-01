import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Continuously Moving Rectangle Example')

rect_x = 400
rect_y = 300
rect_width = 50
rect_height = 30
rect_color = (0, 128, 255)
rect_speed = 5

up_pressed = False
down_pressed = False

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_x -= rect_speed
            elif event.key == pygame.K_RIGHT:
                rect_x += rect_speed
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    if up_pressed:
        rect_y -= rect_speed
    if down_pressed:
        rect_y += rect_speed

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

    clock.tick(60)
