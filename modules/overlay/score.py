# score.py
import pygame
from modules.config import Config
from modules.color import Color

class Score:
    def __init__(self, x, y, player_score) -> None:
        self.x = x
        self.y = y

        self.text = Config.FONT.render(f"{player_score}", True, Color.WHITE)

    def update(self, player_score):
        self.text = Config.FONT.render(f"{player_score}", True, Color.WHITE)

    def draw(self, surface):
        pygame.display.set_caption
        surface.blit(self.text, (self.x, self.y))