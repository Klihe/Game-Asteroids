# projectile.py
import pygame
import math

class Projectile:
    def __init__(self, center, angle, speed) -> None:
        self.center = center
        self.angle = angle
        self.damage = 15
        self.movement_speed = 25 + speed

        self.image = pygame.image.load("source/playing/bullet.png")
        self.rect = self.image.get_rect(center=(self.center))

    def movement(self) -> None:
        self.rect.x += int(self.movement_speed * math.sin(math.radians(self.angle)))
        self.rect.y += int(self.movement_speed * math.cos(math.radians(self.angle)))
    
    def update(self) -> None:
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)