# game.py
import pygame
from modules.config import Config
from modules.color import Color

from modules.game_state.game_state import Game_State
from modules.game_state.menu import Menu
from modules.game_state.playing import Playing
from modules.game_state.game_over import Game_over

from modules.player.player import Player

class Game:
    def __init__(self) -> None:
        self.game_state = Game_State.PLAYING

        self.player = Player(Config.WINDOW_WIDTH//2 - 60, Config.WINDOW_HEIGHT//2 - 60, 0, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)
    
    def update(self, time, keys):

        if self.game_state == Game_State.MENU:
            pass

        elif self.game_state == Game_State.PLAYING:
            self.player.movement(keys)
            # self.player.fire(keys)
            self.player.update()

        elif self.game_state == Game_State.GAME_OVER:
            pass

    def draw(self, surface):

        if self.game_state == Game_State.MENU:
            pass

        elif self.game_state == Game_State.PLAYING:
            surface.fill(Color.BLACK)
            self.player.draw(surface)

        elif self.game_state == Game_State.GAME_OVER:
            pass