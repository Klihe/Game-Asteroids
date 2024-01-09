# high_score.py
from modules.config import Config
from modules.color import Color

class High_Score:

    def read(self) -> None:
        with open("save/high_score.txt", "r") as file:
            self.high_score = file.read()

    def save(self, score) -> None:
        if score > int(self.high_score):
            self.high_score = score
        with open("save/high_score.txt", "w") as file:
            file.write("")
        with open("save/high_score.txt", "a") as file:
            file.write(str(score))

    def draw(self, surface) -> None:
        text = Config.FONT.render(f"High Score: {self.high_score}", True, Color.WHITE)
        surface.blit(text, (10, 10))