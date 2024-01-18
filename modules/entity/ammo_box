# asteroids.py

import pygame
import random
import math
from modules.config import Config

class Ammo_box:
    def __init__(self) -> None:
        self.x = random.choice([random.randint(100, 500), random.randint(1500, 1820)])
        self.y = random.choice([random.randint(100, 500), random.randint(750, 980)])

        self.speed = 0
        self.angle = random.randint(1, 359)
        self.rotate = random.randint(1, 359)       

        self.ammo = 50

        self.src_image = pygame.image.load("source/playing/asteroid/" + self.size + ".png")
        self.image = pygame.transform.rotate(self.src_image, self.rotate)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def check_collision_asteroid(self, other_asteroid) -> None:
        if self.rect.colliderect(other_asteroid.rect):
            self.angle += 30

    def update(self) -> None:
        self.rotate += 1

        if self.x > Config.WINDOW_WIDTH - self.rect.width or self.x < 0 or self.y > Config.WINDOW_HEIGHT - self.rect.height or self.y < 0:
            self.angle += 45
            self.speed = -self.speed

        self.x += int(self.speed * math.sin(math.radians(self.angle)))
        self.y += int(self.speed * math.cos(math.radians(self.angle)))

        self.image = pygame.transform.rotate(self.image, self.rotate)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface) -> None:
        surface.blit(self.image, self.rect)