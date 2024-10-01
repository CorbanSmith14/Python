import pygame
from pygame import Color

class RuleScreen:
    def __init__(self):
        self.text_color = Color("white")
        self.background_color = Color("black")
        self.rules = [
            "Welcome to Era Warfare!",
            "The objective is to defend your base and",
            "destroy as many enemy troops as possible.",
            "",
            "Controls:",
            "  - Press 'R' to view these rules.",
            "  - Click the left mouse button to spawn troops.",
            "",
            "Troop Information:",
            "  - Green troops are yours.",
            "  - Red troops are enemies.",
            "  - Troops will attack the enemy base.",
            "",
            "Health Bar:",
            "  - Your base's health is on the left.",
            "  - Enemy base's health is on the right.",
            "  - Bases lose health when troops collide.",
            "",
            "Game Over:",
            "  - The game ends when a base's health reaches 0.",
            "  - Your final score is displayed at the end.",
            "",
            "Enjoy the game!",
            "",
            "Press 'R' to close this screen and start playing.",
        ]

    def display_rules(self, screen):
        screen.fill(self.background_color)
        font_size = 18
        font = pygame.font.Font(None, font_size)

        line_height = 20  # Adjust the spacing between lines
        max_lines = (HEIGHT - 50) // line_height

        for i, line in enumerate(self.rules[:max_lines]):
            text = font.render(line, True, self.text_color)
            text_rect = text.get_rect(center=(WIDTH // 2, 30 + i * line_height))
            screen.blit(text, text_rect)

        pygame.display.flip()

    def run_rule_screen(self, screen):
        self.display_rules(screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    running = False


WIDTH, HEIGHT = 564, 317
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Era Warfare Rules")

rule_screen = RuleScreen()
rule_screen.run_rule_screen(screen)

pygame.quit()
