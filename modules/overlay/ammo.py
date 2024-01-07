# ammo.py
import pygame

class Ammo:
    def __init__(self, x, y, ammo):
        self.x = x
        self.y = y
        self.ammo = ammo

        self.image = pygame.image.load("source/playing/ammo/10.png")

    def ammo_minus(self):
        self.ammo -= 1

    def update(self):
        self.image = pygame.image.load("source/playing/ammo/" + f"{self.ammo}" + ".png")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))