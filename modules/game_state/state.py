# state.py
from enum import Enum

class Game_State(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3