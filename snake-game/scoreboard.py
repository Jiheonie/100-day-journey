from turtle import Turtle, Screen


screen = Screen()


SCOREBOARD_HEIGHT = screen.window_height() / 2 - 50

ALIGNMENT = "center"
FONT_STYLE = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(0, SCOREBOARD_HEIGHT)
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}" , align=ALIGNMENT, font=FONT_STYLE)


    def reset(self):
        self.game_over = True
        self.home()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()



