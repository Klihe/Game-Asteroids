# asteroids.py
import pygame
import random
import math

class Asteroid:
    def __init__(self, x, y, radius, angle_start):
        self.x = x
        self.y = y
        self.radius = radius

        self.movement_speed = 5
        self.angle_start = angle_start
        self.angle = random.randint(0, 360)
        
        self.image = pygame.image.load("source/asteroid.png")
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))

    def movement(self):
        self.angle += 1
        self.x += int(self.movement_speed * math.sin(math.radians(self.angle_start)))
        self.y += int(self.movement_speed * math.cos(math.radians(self.angle_start)))

    def update(self):
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_center = self.image_rotate.get_rect(center=self.image_coordinates.center)
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image_rotate, self.image_center)