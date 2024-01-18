# game.py
import pygame
from modules.config import Config
from modules.color import Color
from modules.game_state.state import Game_State
from modules.game_state.menu import Menu
from modules.game_state.game_over import Game_Over
from modules.player.player import Player
from modules.player.player_overlay import Player_overlay
from modules.file.high_score import High_Score
from modules.spirits.asteroid import Asteroid

class Game:
    def __init__(self) -> None:
        self.state = Game_State.MENU
        self.menu = Menu(Config.WINDOW_WIDTH//2, Config.WINDOW_HEIGHT - 125)
        self.game_over = Game_Over(Config.WINDOW_WIDTH//2, Config.WINDOW_HEIGHT//2)
        self.high_score = High_Score()

        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_r)
        self.player_overlay = Player_overlay()

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
                if asteroid.health <= 0:
                    self.player.score += asteroid.score
                    self.asteroids.pop(self.asteroids.index(asteroid))

            for i, asteroid1 in enumerate(self.asteroids):
                for j, asteroid2 in enumerate(self.asteroids):
                    if i != j:
                        asteroid1.check_collision_asteroid(asteroid2)

            for asteroid in self.asteroids:
                asteroid.check_collision_asteroid(self.player)

            self.player.update()
            self.player.movement(keys)
            self.player.combat(keys, time)
            self.player_overlay.update(self.player.magazine, self.player.health, self.player.score)
            
            if self.player.health <= 0:
                self.state = Game_State.GAME_OVER

        elif self.state == Game_State.GAME_OVER:
            self.high_score.save(self.player.score)

    def draw(self, surface) -> None:
        if self.state == Game_State.MENU:
            self.menu.draw(surface)

        elif self.state == Game_State.PLAYING:
            surface.fill(Color.BLACK)
            self.player.draw(surface)

            for asteroid in self.asteroids:
                asteroid.draw(surface)
                
            self.player_overlay.draw(surface)

        elif self.state == Game_State.GAME_OVER:
            self.game_over.draw(surface, self.player.score)
            self.high_score.draw(surface)