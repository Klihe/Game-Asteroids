# asteroids.py
import pygame
import random
import math
from modules.config import Config
class Asteroid:
    def __init__(self) -> None:
        self.x = random.choice([random.randint(100, 500), random.randint(1500, 1820)])
        self.y = random.choice([random.randint(100, 500), random.randint(750, 980)])
        self.size = random.choice(["small", "medium", "large"])

        self.movement_speed = random.randint(5, 7)
        self.direction = random.randint(1, 359)
        self.angle_rotate = random.randint(1, 359)       

        if self.size == "small":
            self.health = 15
            self.damage = 10
        elif self.size == "medium":
            self.health = 30
            self.damage = 15
        elif self.size == "large":
            self.health = 45       
            self.damage = 20

        self.image = pygame.image.load("source/playing/asteroid/" + self.size + ".png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image_rotate = pygame.transform.rotate(self.image, self.angle_rotate)

    def movement(self) -> None:
        if self.rect.x > Config.WINDOW_WIDTH - self.rect.width or self.rect.x < 0 or self.rect.y > Config.WINDOW_HEIGHT - self.rect.height or self.rect.y < 0:
            self.direction += 45
            self.movement_speed = -self.movement_speed

        self.rect.x += int(self.movement_speed * math.sin(math.radians(self.direction)))
        self.rect.y += int(self.movement_speed * math.cos(math.radians(self.direction)))

    def check_collision_asteroid(self, other_asteroid) -> None:
        if self.rect.colliderect(other_asteroid.rect):
            self.direction += 30

    def update(self) -> None:
        self.angle_rotate += 1
        self.image_rotate = pygame.transform.rotate(self.image, self.angle_rotate)

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)