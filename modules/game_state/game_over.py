# game_over.py
import pygame
from modules.color import Color

class Game_Over:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.start_button_image = pygame.image.load("source/menu/game_over.png")
        self.start_button_rect = self.start_button_image.get_rect(center=(self.x, self.y))

    def draw(self, surface) -> None:
        surface.fill(Color.BLACK)
        surface.blit(self.start_button_image, self.start_button_rect)