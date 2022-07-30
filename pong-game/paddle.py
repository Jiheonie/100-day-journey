from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")


UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


    def control(self, up_key, down_key):
        screen.listen()
        screen.onkeypress(self.up, up_key)
        screen.onkeypress(self.down, down_key)
        screen.onkeypress(screen.bye, "space")
