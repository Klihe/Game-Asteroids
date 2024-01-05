# player.py
import pygame
import math
import sys

class Player:
    def __init__(self, x, y, width, height, straight, left, right):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0

        self.rotation_speed = 5
        self.movement_speed = 10

        self.straight = straight
        self.left = left
        self.right = right

        self.image = pygame.image.load("source/rocket.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def movement(self, keys):
        if keys[self.straight]:
            self.x += int(self.movement_speed * math.sin(math.radians(self.angle)))
            self.y += int(self.movement_speed * math.cos(math.radians(self.angle)))

        if keys[self.left]:
            self.angle += self.rotation_speed
        if keys[self.right]:
            self.angle -= self.rotation_speed

    def update(self):
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect_rotate = self.image_rotate.get_rect(center=self.rect.center)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image_rotate, self.rect_rotate)