# main.py
import pygame
from modules.config import Config
from modules.game import Game

pygame.init()

window_main = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")

clock = pygame.time.Clock()
running = True

game = Game()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update(pygame.key.get_pressed(), pygame.time.get_ticks())
    game.draw(window_main)

    pygame.display.flip()


pygame.quit()