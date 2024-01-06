# health_bar.py
import pygame

class Health_Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, health):
        if health <= 10:
            color = "black"
        elif health <= 50:
            color = "red"
        elif health <= 70:
            color = "orange"
        elif health <= 90:
            color = "yellow"
        elif health <= 100:
            color = "green"

        self.image = pygame.image.load("source/health_bar/" + color + ".png")
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
