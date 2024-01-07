# game_over.py
import pygame
from modules.color import Color
from modules.config import Config

class Game_Over:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.start_button_image = pygame.image.load("source/menu/game_over.png")
        self.start_button_rect = self.start_button_image.get_rect(center=(self.x, self.y))

    def draw(self, surface, player_score) -> None:
        surface.fill(Color.BLACK)
        surface.blit(self.start_button_image, self.start_button_rect)
        self.text = Config.FONT.render(f"Your score: {player_score}", True, Color.WHITE)
        surface.blit(self.text, (self.x - 100, self.y + 100))