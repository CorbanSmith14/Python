import pygame
import sys
import random
import os
import menu
from rule import RuleScreen

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 564, 317
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player Base
player_base_width, player_base_height = 20, HEIGHT // 10
player_base_x = 0
player_base_y = HEIGHT - player_base_height - 20
player_base_health = 100
player_spawn_interval = 60  # frames between unit spawns
player_spawn_timer = player_spawn_interval

# Enemy Base
enemy_base_width, enemy_base_height = 20, HEIGHT // 10
enemy_base_x = WIDTH - enemy_base_width
enemy_base_y = HEIGHT - player_base_height - 20
enemy_base_health = 100
enemy_spawn_interval = 90  # frames between enemy spawns
enemy_spawn_timer = enemy_spawn_interval

# Units
player_units = []
enemy_units = []

# Initialize score and timer
score = 0
start_time = pygame.time.get_ticks()

# Button
button_width, button_height = 200, 40
button_x, button_y = WIDTH // 2 - button_width // 2, 0
button_color = (0, 255, 0)
button_clicked = False

# Load spearman image
spearman_image = pygame.image.load(os.path.join("images-sounds", "spear-man.png"))
spearman_image = pygame.transform.scale(spearman_image, (40, 20))

# Load background image
background_image = pygame.image.load(os.path.join("images-sounds", "background.jpg"))
background_image = pygame.transform.scale(background_image, (564, 317))

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(os.path.join("images-sounds", "Era Warfare"))
clock = pygame.time.Clock()

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize rule screen
rule_screen = RuleScreen()

# Load background music and battle sounds
background_music = pygame.mixer.Sound(os.path.join("images-sounds", "background-music.mp3"))
background_music.set_volume(0.3)
battle_cry_sound = pygame.mixer.Sound(os.path.join("images-sounds", "battle-cry.wav"))
battle_cry_sound.set_volume(10.0)
sword_strike_sound = pygame.mixer.Sound(os.path.join("images-sounds", "sword-strike.wav"))
sword_strike_sound.set_volume(1.0)


def check_collision(unit1, unit2):
    return (
        unit1[0] < unit2[0] + spearman_image.get_width()
        and unit1[0] + spearman_image.get_width() > unit2[0]
        and unit1[1] < unit2[1] + spearman_image.get_height()
        and unit1[1] + spearman_image.get_height() > unit2[1]
    )


class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


def game_over_screen(final_score):
    screen.fill(WHITE)  
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, RED)
    score_text = font.render(f"Final Score: {final_score}", True, BLUE)

    # Center the text on the screen
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

    pygame.display.flip()
    pygame.time.delay(3000)  # Display the game over screen for 3 seconds


# Menu loop
main_menu = menu.GameMenu()
while main_menu.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rule_screen.run_rule_screen(screen)

    main_menu.run()

# Play music
background_music.play(-1)

# Game loop
running = True
button = Button(button_x, button_y, button_width, button_height, button_color, "Spawn Troops")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            if button.rect.collidepoint(event.pos):
                button_clicked = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rule_screen.run_rule_screen(screen)

    # timer
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000  # Convert to seconds

    # Update score
    for enemy_unit in enemy_units[:]:
        if enemy_unit[3] <= 0 and enemy_unit[4]:
            # Increment score only if the enemy troop is destroyed and moving
            score += 1
            enemy_unit[4] = False  # stop moving

    # Remove destroyed enemy units
    enemy_units = [unit for unit in enemy_units if unit[3] > 0]

    # Player base logic
    player_spawn_timer -= 1
    if player_spawn_timer <= 0 and button_clicked:
        player_units.append([player_base_x, player_base_y, 5, 10, True])  # x, y, speed, damage, moving
        player_spawn_timer = player_spawn_interval
        button_clicked = False
        # Play the battle cry sound
        battle_cry_sound.play()

    # Enemy base logic
    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        enemy_units.append([enemy_base_x - 40, player_base_y, -3, 10, True])  # x, y, speed, damage, moving
        enemy_spawn_timer = enemy_spawn_interval

    # Update units
    for unit in player_units:
        if unit[4]:  # Check if the unit is moving
            unit[0] += unit[2]
            if unit[0] > WIDTH - 50:  # reached the enemy base
                unit[4] = False  # stop moving

    for unit in enemy_units:
        if unit[4]:  # Check if the unit is moving
            unit[0] += unit[2]
            if unit[0] < 0:  # reached the player base
                unit[4] = False  # stop moving

    # Check for unit collisions
    for player_unit in player_units:
        for enemy_unit in enemy_units:
            if check_collision(player_unit, enemy_unit):
                player_unit[4] = False  # stop moving
                enemy_unit[4] = False  # stop moving

                player_unit[3] -= 1  # reduce the player unit's health
                enemy_unit[3] -= 1   # reduce the enemy unit's health

                # Play the sword strike sound
                sword_strike_sound.play()

                if player_unit[3] <= 0:
                    player_units.remove(player_unit)

                if enemy_unit[3] <= 0:
                    enemy_units.remove(enemy_unit)

    # Update bases' health based on troop collisions
    for player_unit in player_units:
        if check_collision((player_unit[0], player_unit[1]), (enemy_base_x, enemy_base_y, enemy_base_width, enemy_base_height)):
            enemy_base_health -= 1
            player_units.remove(player_unit)

    for enemy_unit in enemy_units:
        if check_collision((enemy_unit[0], enemy_unit[1]), (player_base_x, player_base_y, player_base_width, player_base_height)):
            player_base_health -= 1
            enemy_units.remove(enemy_unit)

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw player units
    for unit in player_units:
        screen.blit(spearman_image, (unit[0], unit[1]))

    # Draw enemy units
    for unit in enemy_units:
        screen.blit(spearman_image, (unit[0], unit[1]))

    # Draw everything else
    pygame.draw.rect(screen, RED, (player_base_x, player_base_y, player_base_width, player_base_height))
    pygame.draw.rect(screen, BLUE, (enemy_base_x, enemy_base_y, enemy_base_width, enemy_base_height))

    # Draw the health bars
    pygame.draw.rect(screen, RED, (50, HEIGHT - 20, max(0, player_base_health * 2), 20))
    pygame.draw.rect(screen, BLUE, (WIDTH - 50 - max(0, enemy_base_health * 2), HEIGHT - 20, max(0, enemy_base_health * 2), 20))

    # Draw the button
    button.draw(screen)

    # Draw the score and timer
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {elapsed_time}s", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (WIDTH - 150, 10))

    # Check for game over
    if player_base_health <= 0 or enemy_base_health <= 0:
        print("Game Over!")
        background_music.stop()
        game_over_screen(score)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
