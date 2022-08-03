from turtle import Turtle


ALIGNMENT = "center"
FONT_STYLE = ('Arial', 60, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT_STYLE)
        