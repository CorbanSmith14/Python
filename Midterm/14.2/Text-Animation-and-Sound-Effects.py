import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))

# Initialize the font module
pygame.font.init()

# Create a font object using 'freesansbold'
font = pygame.font.SysFont('freesansbold', 36)

# Render the text. "True" means anti-aliased text.
text = font.render("Hello, Pygame!", True, (255, 255, 255))

# Initial position and velocity of the text
text_position = [400 - text.get_width() // 2, 300 - text.get_height() // 2]
text_velocity = [5, 5]  # Change in x and y for each frame

# Load sound effect
bounce_sound = pygame.mixer.Sound("bounce.wav")

# Continuous background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # -1 means play the music indefinitely

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update text position based on velocity
    text_position[0] += text_velocity[0]
    text_position[1] += text_velocity[1]

    # Bounce off screen edges and change color
    if text_position[0] <= 0 or text_position[0] + text.get_width() >= 800:
        text_velocity[0] = -text_velocity[0]
        text.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        bounce_sound.play()

    if text_position[1] <= 0 or text_position[1] + text.get_height() >= 600:
        text_velocity[1] = -text_velocity[1]
        text.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        bounce_sound.play()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the text onto the screen
    screen.blit(text, text_position)

    # Update the display
    pygame.display.update()

    # Control the frame rate (you can adjust this value)
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
