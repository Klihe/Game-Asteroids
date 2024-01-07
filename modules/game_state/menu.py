# menu.py
import pygame

class Menu:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.start_button_image = pygame.image.load("source/menu/start/passive.png")
        self.start_button_rect = self.start_button_image.get_rect(center=(self.x, self.y))
        
    def update(self, mouse_position, mouse_pressed) -> None:
        if self.start_button_rect.collidepoint(mouse_position):
            self.start_button_image = pygame.image.load("source/menu/start/active.png")
            if mouse_pressed[0]:
                return 1
        else:
            self.start_button_image = pygame.image.load("source/menu/start/passive.png")
        return 0

    def draw(self, surface) -> None:
        surface.blit(self.start_button_image, self.start_button_rect)