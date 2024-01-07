# health_bar.py
import pygame

class Health_Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = pygame.image.load("source/playing/health_bar/100.png")

    def update(self, health):
        if health <= 10:
            color = "10"
        elif health <= 20:
            color = "20"
        elif health <= 30:
            color = "30"
        elif health <= 40:
            color = "40"
        elif health <= 50:
            color = "50"
        elif health <= 60:
            color = "60"
        elif health <= 70:
            color = "70"
        elif health <= 80:
            color = "80"
        elif health <= 90:
            color = "90"
        elif health <= 100:
            color = "100"
    
        self.image = pygame.image.load("source/playing/health_bar/" + color + ".png")
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
