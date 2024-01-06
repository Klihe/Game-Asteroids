# player.py
import pygame
import math

class Player:
    def __init__(self, x, y, key_straight, key_left, key_right) -> None:
        self.x = x
        self.y = y
        self.angle = 0

        self.damage_detection_cooldown = 1000
        self.last_damage = 0

        self.health = 100
        self.rotation_speed_current = 0
        self.rotation_speed_max = 30
        self.movement_speed_current = 0
        self.movement_speed_max = 7

        self.key_straight = key_straight
        self.key_left = key_left
        self.key_right = key_right

        self.image = pygame.image.load("source/rocket.png")

    def movement(self, keys) -> None:
        if keys[self.key_straight] and self.movement_speed_current < self.movement_speed_max:
            self.movement_speed_current += 0.5
        elif self.movement_speed_current > 0:
            self.movement_speed_current -= 0.25

        self.x += int(self.movement_speed_current * math.sin(math.radians(self.angle)))
        self.y += int(self.movement_speed_current * math.cos(math.radians(self.angle)))

        if keys[self.key_left] and self.rotation_speed_current < self.rotation_speed_max:
            self.rotation_speed_current += 3
        elif keys[self.key_right] and self.rotation_speed_current > -self.rotation_speed_max:
            self.rotation_speed_current -= 3
        elif self.rotation_speed_current != 0:
            self.rotation_speed_current += 3 if self.rotation_speed_current < 0 else -3

        self.angle += self.rotation_speed_current / 10

    def check_collision(self, other_spirit) -> None:
        if self.damage_detection_cooldown < pygame.time.get_ticks() - self.last_damage:
            if self.rect.colliderect(other_spirit.rect):
                self.last_damage = pygame.time.get_ticks()
                self.health -= other_spirit.damage
                print(self.health)
                self.image = pygame.image.load("source/rocket_hit.png")
            else:
                self.image = pygame.image.load("source/rocket.png")

    def update(self) -> None:
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect(center=(self.x, self.y))

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)