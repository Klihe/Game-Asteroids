# player.py

import pygame
import math
from modules.config import Config

from modules.player.bullet import Bullet

from pygame import sprite
from pygame import mask

class Player(sprite.Sprite):
    def __init__(self, x, y, angle, k_up, k_down, k_left, k_right, k_fire) -> None:
        super().__init__()
        # position
        self.position = {
            # basic
            "x" : x,
            "y" : y,

            # advance
            "angle" : angle
        }

        # stats
        self.stats = {
            "multi_speed" : 1,
            "health" : 100,
            "body_damage" : 15
        }

        # ammo
        self.ammo = {
            # object
            "bullets" : [],

            "max" : 3,
            "magazine" : 10
        }

        # keys
        self.keys = {
            # movement
            "up" : k_up,
            "down" : k_down,
            "left" : k_left,
            "right" : k_right,

            # others actions
            "fire" : k_fire
        }

        # speed
        self.speed = {
            "current" : 2,
            "max" : 10
        }

        # image/body
        self.source_image = pygame.image.load("source/playing/rocket/rocket.png")
        self.image = pygame.transform.rotate(self.source_image, self.position["angle"])
        self.mask = pygame.mask.from_surface(self.image)
        self.body = self.image.get_rect(center=(self.position["x"], self.position["y"]))

    def movement(self, keys) -> None:
        if keys[self.keys["up"]] and self.speed["current"] < self.speed["max"]:
            self.speed["current"] += 0.25
        elif self.speed["current"] > 2:
            self.speed["current"] -= 0.1

        if keys[self.keys["left"]]:
            self.position["angle"] += self.speed["current"] // 2.5
        elif keys[self.keys["right"]]:
            self.position["angle"] -= self.speed["current"] // 2.5

        self.position["x"] += int(self.speed["current"] * math.sin(math.radians(self.position["angle"])))
        self.position["y"] += int(self.speed["current"] * math.cos(math.radians(self.position["angle"])))

        # minimum/maximum
        self.position["x"] = max(60, min(self.position["x"], Config.WINDOW_WIDTH - 60))
        self.position["y"] = max(60, min(self.position["y"], Config.WINDOW_HEIGHT - 60))

    # def fire(self, keys) -> None:
    #     if keys[self.keys["fire"]]:
    #         self.ammo["bullets"].append(Bullet(self.position["x"], self.position["y"], self.position["angle"], self.speed["current"]))

    def update(self) -> None:
        self.image = pygame.transform.rotate(self.source_image, self.position["angle"])
        self.body = self.image.get_rect(center=(self.position["x"], self.position["y"]))

        # for bullet in self.ammo["bullets"]:
        #     bullet.movement()
        #     bullet.update()

    def draw(self, surface) -> None:
        surface.blit(self.image, self.body)

        # for bullet in self.ammo["bullets"]:
        #     bullet.draw(surface)