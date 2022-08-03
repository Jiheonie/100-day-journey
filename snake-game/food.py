from turtle import Turtle, Screen
from random import randint


screen = Screen()
width_edge = screen.window_width() / 2 - 50
height_edge = screen.window_height() / 2 - 50


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()


    def move(self):
        random_x = randint(width_edge * -1, width_edge)
        random_y = randint(height_edge * -1, height_edge)
        self.goto(random_x, random_y)

