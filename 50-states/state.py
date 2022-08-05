from turtle import Turtle


from turtle import Turtle


class State(Turtle):
    def __init__(self, x, y, guess) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(guess.title(), move=False, align="center")