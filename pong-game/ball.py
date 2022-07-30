from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        first_heading = randint(0, 359)
        self.setheading(first_heading) 
        self.move_speed = 0.05

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        final_heading = 360 - self.heading() 
        self.setheading(final_heading)

    def bounce_paddle(self):
        if self.heading() < 180:
            final_heading = 180 - self.heading()
        else:
            final_heading = 540 - self.heading()
        self.setheading(final_heading)
        self.move_speed *= 0.85

    def miss(self, miss):
        self.goto(0, 0)
        if miss == "left":
            self.setheading(randint(-70, 70))
        else:
            self.setheading(randint(110, 250))
        self.move_speed = 0.05