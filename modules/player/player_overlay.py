# player_overlay.py

import pygame

from modules.config import Config
from modules.color import Color

class Player_overlay:
    def __init__(self):
        self.ammo_image = pygame.image.load("source/playing/ammo/10.png")
        self.health_image = pygame.image.load("source/playing/health_bar/100.png")
        self.score_text = Config.FONT.render(f"{0}", True, Color.WHITE)

    def update(self, ammo, health, score):
        self.ammo = ammo 
        self.health = health
        self.score = score
        
        self.ammo_image = pygame.image.load("source/playing/ammo/" + f"{self.ammo}" + ".png")
        print(self.ammo)

        if self.health <= 10:
            color = "10"
        elif self.health <= 20:
            color = "20"
        elif self.health <= 30:
            color = "30"
        elif self.health <= 40:
            color = "40"
        elif self.health <= 50:
            color = "50"
        elif self.health <= 60:
            color = "60"
        elif self.health <= 70:
            color = "70"
        elif self.health <= 80:
            color = "80"
        elif self.health <= 90:
            color = "90"
        elif self.health <= 100:
            color = "100"
    
        self.health_image = pygame.image.load("source/playing/health_bar/" + color + ".png")

        self.score_text = Config.FONT.render(f"{self.score}", True, Color.WHITE)

    def draw(self, surface):
        surface.blit(self.ammo_image, (Config.WINDOW_WIDTH//2 - 147, Config.WINDOW_HEIGHT - 75))
        surface.blit(self.health_image, (Config.WINDOW_WIDTH//2 - 150, Config.WINDOW_HEIGHT - 45))
        surface.blit(self.score_text, (Config.WINDOW_WIDTH//2 + 35, Config.WINDOW_HEIGHT - 52))