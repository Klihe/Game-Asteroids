# player.py
import pygame
import math
from modules.config import Config

class Player:
    def __init__(self, x, y, k_straight, k_left, k_right, k_fire) -> None:
        # position
        self.x = x
        self.y = y
        self.angle = 0

        self.score = 0
        self.health = 100
        self.body_damage = 15

        self.hit_detection_cooldown = 500
        self.last_hit = 0

        self.rotation_speed = 1.5
        self.movement_speed = 2.5
        self.movement_speed_max = 10

        self.k_straight = k_straight
        self.k_left = k_left
        self.k_right = k_right
        self.k_fire = k_fire

        self.image = pygame.image.load("source/playing/rocket.png")
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect(center=(self.x, self.y))

    def movement(self, keys) -> None:
        # movement
        if keys[self.k_straight] and self.movement_speed < self.movement_speed_max:
            self.movement_speed += 0.25
        elif self.movement_speed > 2.5:
            self.movement_speed -= 0.125

        # rotation
        if keys[self.k_left]:
            self.angle += self.rotation_speed + self.movement_speed // 5
        elif keys[self.k_right]:
            self.angle -= self.rotation_speed + self.movement_speed // 5

    def update(self) -> None:
        self.x += int(self.movement_speed * math.sin(math.radians(self.angle)))
        self.y += int(self.movement_speed * math.cos(math.radians(self.angle)))
        self.x = max(60, min(self.x, Config.WINDOW_WIDTH - 60))
        self.y = max(60, min(self.y, Config.WINDOW_HEIGHT - 60))

        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect(center=(self.x, self.y))


    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)