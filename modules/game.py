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
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid()
        ]

    def update(self):
        self.player.update()
        self.player.movement(pygame.key.get_pressed())

        for asteroid in self.asteroids:
            asteroid.update()
            asteroid.movement()
            self.player.check_collision(asteroid.rect)

        for i, asteroid1 in enumerate(self.asteroids):
            for j, asteroid2 in enumerate(self.asteroids):
                if i != j:
                    asteroid1.check_collision(asteroid2.rect)

    def draw(self, surface):
        surface.fill(Color.BLACK)
        self.player.draw(surface)

        for asteroid in self.asteroids:
            asteroid.draw(surface)
