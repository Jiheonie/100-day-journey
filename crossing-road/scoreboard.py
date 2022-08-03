from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over!", move=False, align="center", font=FONT)