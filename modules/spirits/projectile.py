# projectile.py
import pygame
import math

class Projectile:
    def __init__(self, x, y, angle, speed) -> None:
        self.x = x
        self.y = y
        self.angle = angle
        self.movement_speed = 25 + speed

        self.image = pygame.image.load("source/bullet.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def movement(self) -> None:
        self.x += int(self.movement_speed * math.sin(math.radians(self.angle)))
        self.y += int(self.movement_speed * math.cos(math.radians(self.angle)))

        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self) -> None:
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)