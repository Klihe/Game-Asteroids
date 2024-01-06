# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.spirits.player import Player
from modules.overlay.health_bar import Health_Bar
from modules.spirits.projectile import Projectile
from modules.overlay.ammo import Ammo
from modules.spirits.asteroid import Asteroid

class Game:
    def __init__(self) -> None:
        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, pygame.K_w, pygame.K_a, pygame.K_d)
        self.health_bar = Health_Bar(Config.WINDOW_WIDTH//2 - 150, Config.WINDOW_HEIGHT - 45)
        self.bullet_magazine = Ammo(Config.WINDOW_WIDTH//2 - 147, Config.WINDOW_HEIGHT - 75, 10)

        self.bullets = []
        self.bullet_reload_cooldown = 1000
        self.bullet_reload_last = 1000
        self.bullet_reloading = False
        self.bullet_fire_cooldown = 125
        self.bullet_fire_last = 0

        self.asteroids = [
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid(),
            Asteroid()
        ]

    def update(self, keys, time) -> None:
        self.health_bar.update(self.player.health)

        if int(time) % 100 == 0:
            self.asteroids.append(Asteroid())
        
        if self.bullet_fire_cooldown < time - self.bullet_fire_last and len(self.bullets) < 3:
            if keys[pygame.K_SPACE] and self.bullet_magazine.ammo > 0 and not self.bullet_reloading:
                self.bullet_magazine.ammo_minus()
                self.bullets.append(Projectile(self.player.rect.center, self.player.angle, self.player.movement_speed_current))
                self.bullet_fire_last = time
        for bullet in self.bullets:
            if bullet.rect.x > Config.WINDOW_WIDTH or bullet.rect.x < 0 or bullet.rect.y > Config.WINDOW_HEIGHT or bullet.rect.y < 0:
                self.bullets.pop(self.bullets.index(bullet))

        if self.bullet_reload_cooldown < time - self.bullet_reload_last and self.bullet_reloading:
            self.bullet_reload_last = time
            self.bullet_magazine.ammo = 10
            self.bullet_reloading = False
        elif (keys[pygame.K_r] and self.bullet_magazine.ammo < 10) or (self.bullet_magazine.ammo == 0) and not self.bullet_reloading:
            self.bullet_reloading = True
            self.bullet_reload_last = time

        self.player.action(keys)
        self.player.update()
        self.bullet_magazine.update()

        for bullet in self.bullets:
            bullet.movement()
            bullet.update()

        for asteroid in self.asteroids:
            asteroid.movement()
            asteroid.update()
            self.player.check_collision(asteroid, time)
            if asteroid.health <= 0:
                self.asteroids.pop(self.asteroids.index(asteroid))

        for i, asteroid1 in enumerate(self.asteroids):
            for j, asteroid2 in enumerate(self.asteroids):
                if i != j:
                    asteroid1.check_collision_asteroid(asteroid2)

        for asteroid in self.asteroids:
            asteroid.check_collision_asteroid(self.player)

        for asteroid in self.asteroids:
            for bullet in self.bullets:
                if asteroid.rect.colliderect(bullet.rect):
                    asteroid.health -= bullet.damage
                    self.bullets.pop(self.bullets.index(bullet))


    def draw(self, surface) -> None:
        surface.fill(Color.BLACK)

        for bullet in self.bullets:
            bullet.draw(surface)

        self.player.draw(surface)

        for asteroid in self.asteroids:
            asteroid.draw(surface)
            
        self.health_bar.draw(surface)
        self.bullet_magazine.draw(surface)