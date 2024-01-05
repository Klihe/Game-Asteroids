# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.spirits.player import Player
from modules.spirits.asteroid import Asteroid

class Game:
    def __init__(self):
        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, 120, 120, pygame.K_w, pygame.K_a, pygame.K_d)

        self.asteroids = [
            Asteroid(100, 500, 30, 90),
            Asteroid(200, 400, 30, 80),
            Asteroid(300, 300, 30, 70),
            Asteroid(400, 200, 30, 60),
            Asteroid(500, 100, 30, 50)
        ]

    def update(self):
        self.player.update()
        self.player.movement(pygame.key.get_pressed())

        for asteroid in self.asteroids:
            asteroid.update()
            asteroid.movement()

    def draw(self, surface):
        surface.fill(Color.BLACK)
        self.player.draw(surface)

        for asteroid in self.asteroids:
            asteroid.draw(surface)
