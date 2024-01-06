# asteroids.py
import pygame
import random
import math
from modules.config import Config
class Asteroid:
    def __init__(self):
        self.x = random.choice([random.randint(0, 500), random.randint(1500, 1920)])
        self.y = random.choice([random.randint(0, 500), random.randint(750, 1080)])

        self.movement_speed = random.randint(5, 7)
        self.angle_start = random.randint(1, 359)
        self.angle = random.randint(1, 359)
        
        self.image = pygame.image.load("source/asteroid.png")
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

    def movement(self):
        if self.x > Config.WINDOW_WIDTH or self.x < 0 or self.y > Config.WINDOW_HEIGHT or self.y < 0:
            self.angle_start += 45

        self.x += int(self.movement_speed * math.sin(math.radians(self.angle_start)))
        self.y += int(self.movement_speed * math.cos(math.radians(self.angle_start)))

        self.rect.x = self.x
        self.rect.y = self.y

    def check_collision(self, other_spirit):
        if self.rect.colliderect(other_spirit):
            self.angle_start += 45

    def update(self):
        self.angle += 1
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_center = self.image_rotate.get_rect(center=self.image_coordinates.center)
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        surface.blit(self.image_rotate, self.image_center)