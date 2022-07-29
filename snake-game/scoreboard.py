from turtle import Turtle, Screen


screen = Screen()


SCOREBOARD_HEIGHT = screen.window_height() / 2 - 50

ALIGNMENT = "center"
FONT_STYLE = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, SCOREBOARD_HEIGHT)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}" , align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.home()
        self.write("GAME OVER!" , align=ALIGNMENT, font=FONT_STYLE)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()



