# bullet.py

import pygame
import math

class Bullet:
    def __init__(self, x, y, angle, speed) -> None:
        # position
        self.position = {
            "x" : x,
            "y" : y,
            "angle" : angle
        }

        # stats
        self.stats = {
            "damage" : 15,
            "health" : 15,
            "speed" : 25 + speed
        }

        self.source_image = pygame.image.load("source/playing/bullet.png")
        self.image = pygame.transform.rotate(self.source_image, self.position["angle"])
        self.mask = pygame.mask.from_surface(self.image)
        self.body = self.image.get_rect(center=(self.position["x"], self.position["y"]))

    def movement(self) -> None:
        self.position["x"] += int(self.stats["speed"] * math.sin(math.radians(self.position["angle"])))
        self.position["y"] += int(self.stats["speed"] * math.cos(math.radians(self.position["angle"])))

    def update(self) -> None:
        self.image = pygame.transform.rotate(self.source_image, self.position["angle"])
        self.body = self.image.get_rect(center=(self.position["x"], self.position["y"]))

    def draw(self, surface) -> None:
        surface.blit(self.image, self.body)
