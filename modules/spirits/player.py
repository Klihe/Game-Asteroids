# player.py
import pygame
import math

class Player:
    def __init__(self, x, y, width, height, straight, left, right):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0

        self.rotation_speed_current = 0
        self.rotation_speed_max = 3
        self.movement_speed_current = 0
        self.movement_speed_max = 10

        self.straight = straight
        self.left = left
        self.right = right

        self.image = pygame.image.load("source/rocket.png")
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))

    def movement(self, keys):
        if keys[self.straight] and self.movement_speed_current < self.movement_speed_max:
            self.movement_speed_current += 0.5
        elif self.movement_speed_current > 0:
            self.movement_speed_current -= 0.25

        self.x += int(self.movement_speed_current * math.sin(math.radians(self.angle)))
        self.y += int(self.movement_speed_current * math.cos(math.radians(self.angle)))

        if self.rotation_speed_current >= 0:
            if keys[self.left] and self.rotation_speed_current < self.rotation_speed_max:
                self.rotation_speed_current += 0.2
            elif self.rotation_speed_current != 0:
                self.rotation_speed_current -= 0.2
        if self.rotation_speed_current <= 0:
            if keys[self.right] and self.rotation_speed_current > self.rotation_speed_max * -1:
                self.rotation_speed_current -= 0.2
            elif self.rotation_speed_current != 0:
                self.rotation_speed_current += 0.2
        self.angle += self.rotation_speed_current

    def update(self):
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_center = self.image_rotate.get_rect(center=self.image_coordinates.center)
        self.image_coordinates = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image_rotate, self.image_center)