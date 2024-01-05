# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.spirits.player import Player

class Game:
    def __init__(self):
        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, 120, 120, pygame.K_w, pygame.K_a, pygame.K_d)

    def update(self):
        self.player.update()
        self.player.movement(pygame.key.get_pressed())

    def draw(self, surface):
        surface.fill(Color.BLACK)
        self.player.draw(surface)
