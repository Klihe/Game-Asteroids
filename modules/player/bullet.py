# bullet.py
import pygame
import math

class Bullet:
    def __init__(self, center, angle, speed) -> None:
        # position
        self.x, self.y = center
        self.angle = angle

        # stats
        self.speed = 25 + speed
        self.damage = 15
        self.health = 15

        # body/image
        self.src_image = pygame.image.load("source/playing/bullet.png")
        self.image = pygame.transform.rotate(self.src_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self) -> None:
        # update position
        self.x += int(self.speed * math.sin(math.radians(self.angle)))
        self.y += int(self.speed * math.cos(math.radians(self.angle)))

        # update image
        self.image = pygame.transform.rotate(self.src_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface) -> None:
        # draw image
        surface.blit(self.image, self.rect)
