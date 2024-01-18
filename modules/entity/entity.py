# entity.py

import pygame
import math

from modules.config import Config

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = None
        self.angle = None
        self.rotate = self.speed / 2

        self.image = None
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x += int(self.speed * math.sin(math.radians(self.angle)))
        self.y += int(self.speed * math.cos(math.radians(self.angle)))

        # boarders
        self.x = max(60, min(self.x, Config.WINDOW_WIDTH - 60))
        self.y = max(60, min(self.y, Config.WINDOW_HEIGHT - 60))

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)