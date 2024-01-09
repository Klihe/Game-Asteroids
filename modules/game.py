# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.game_state.state import Game_State
from modules.game_state.menu import Menu
from modules.game_state.game_over import Game_Over
from modules.spirits.player import Player
from modules.overlay.health_bar import Health_Bar
from modules.overlay.score import Score
from modules.file.high_score import High_Score
from modules.spirits.projectile import Projectile
from modules.overlay.ammo import Ammo
from modules.spirits.asteroid import Asteroid

class Game:
    def __init__(self) -> None:
        self.state = Game_State.MENU
        self.menu = Menu(Config.WINDOW_WIDTH//2, Config.WINDOW_HEIGHT - 125)
        self.game_over = Game_Over(Config.WINDOW_WIDTH//2, Config.WINDOW_HEIGHT//2)
        self.high_score = High_Score()

        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, pygame.K_w, pygame.K_a, pygame.K_d)
        self.health_bar = Health_Bar(Config.WINDOW_WIDTH//2 - 150, Config.WINDOW_HEIGHT - 45)
        self.bullet_magazine = Ammo(Config.WINDOW_WIDTH//2 - 147, Config.WINDOW_HEIGHT - 75, 10)
        self.score = Score(Config.WINDOW_WIDTH//2 + 35, Config.WINDOW_HEIGHT - 52, self.player.score)

        self.bullets = []
        self.bullet_reload_cooldown = 750
        self.bullet_reload_last = 750
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

        if self.state == Game_State.MENU:
            self.high_score.read()

            if self.menu.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                self.state = Game_State.PLAYING

        elif self.state == Game_State.PLAYING:

            if len(self.asteroids) < 5:
                if int(time) % 100 == 0:
                    self.asteroids.append(Asteroid())
            else:
                if int(time) % 200 == 0:
                    self.asteroids.append(Asteroid())


            for asteroid in self.asteroids:
                asteroid.movement()
                asteroid.update()
                self.player.check_collision(asteroid, time)
                if asteroid.health <= 0:
                    self.player.score += asteroid.score
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

            self.player.update()
            self.player.action(keys)
            self.score.update(self.player.score)

            self.health_bar.update(self.player.health)
            
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
                if self.bullet_magazine.ammo == 0:
                    self.bullet_reload_last = time + self.bullet_fire_cooldown
                else:
                    self.bullet_reload_last = time
                self.bullet_reloading = True

            self.bullet_magazine.update()

            for bullet in self.bullets:
                bullet.action()
                bullet.update()
            
            if self.player.health <= 0:
                self.state = Game_State.GAME_OVER

        elif self.state == Game_State.GAME_OVER:
            self.high_score.save(self.player.score)

    def draw(self, surface) -> None:
        if self.state == Game_State.MENU:
            self.menu.draw(surface)

        elif self.state == Game_State.PLAYING:
            surface.fill(Color.BLACK)

            for bullet in self.bullets:
                bullet.draw(surface)

            self.player.draw(surface)

            for asteroid in self.asteroids:
                asteroid.draw(surface)
                
            self.health_bar.draw(surface)
            self.bullet_magazine.draw(surface)
            self.score.draw(surface)
        
        elif self.state == Game_State.GAME_OVER:
            self.game_over.draw(surface, self.player.score)
            self.high_score.draw(surface)