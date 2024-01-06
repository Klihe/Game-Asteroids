# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.spirits.player import Player
from modules.spirits.projectile import Projectile
from modules.spirits.asteroid import Asteroid

class Game:
    def __init__(self) -> None:
        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, pygame.K_w, pygame.K_a, pygame.K_d)

        self.bullets = []
        self.bullet_cooldown = 175
        self.bullet_last = 0

        self.asteroids = [
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid()
        ]

    def update(self, keys) -> None:
        
        if self.bullet_cooldown < pygame.time.get_ticks() - self.bullet_last:
            if keys[pygame.K_SPACE]:
                self.bullets.append(Projectile(self.player.center.x, self.player.center.y, self.player.angle, self.player.movement_speed_current))
                self.bullet_last = pygame.time.get_ticks()
            for bullet in self.bullets:
                if bullet.x > Config.WINDOW_WIDTH or bullet.x < 0 or bullet.y > Config.WINDOW_HEIGHT or bullet.y < 0:
                    self.bullets.pop(self.bullets.index(bullet))

        self.player.movement(keys)
        self.player.update()

        for bullet in self.bullets:
            bullet.movement()
            bullet.update()

        for asteroid in self.asteroids:
            asteroid.movement()
            asteroid.update()
            self.player.check_collision(asteroid.rect)

        for i, asteroid1 in enumerate(self.asteroids):
            for j, asteroid2 in enumerate(self.asteroids):
                if i != j:
                    asteroid1.check_collision_asteroid(asteroid2)


    def draw(self, surface) -> None:
        surface.fill(Color.BLACK)

        for bullet in self.bullets:
            bullet.draw(surface)

        self.player.draw(surface)

        for asteroid in self.asteroids:
            asteroid.draw(surface)
