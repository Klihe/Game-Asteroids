# player.py
import pygame
import math

class Player:
    def __init__(self, x, y, key_straight, key_left, key_right) -> None:
        self.x = x
        self.y = y
        self.angle = 0

        self.rotation_speed_current = 0
        self.rotation_speed_max = 30
        self.movement_speed_current = 0
        self.movement_speed_max = 10

        self.key_straight = key_straight
        self.key_left = key_left
        self.key_right = key_right

        self.image = pygame.image.load("source/rocket.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

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

    def fire(self, keys, func) -> None:
        if keys[self.fire]:
            func()

    def check_collision(self, other_spirit) -> None:
        if self.rect.colliderect(other_spirit):
            print("Collision")

    def update(self) -> None:
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_center = self.image_rotate.get_rect(center=self.rect.center)
        
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.image_center)