import pygame
import sys

def draw_concentric_circles(screen, num_circles):
    center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
    circle_color = (255, 255, 255)  

    for i in range(num_circles):
        radius = 20 * (i + 1)  # Adjust the factor 20 to change the size of the circles
        pygame.draw.circle(screen, circle_color, (center_x, center_y), radius, 1)  # 1 indicates circle outline

    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Concentric Circles')

    num_circles = 5  # number of circles
    draw_concentric_circles(screen, num_circles)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
