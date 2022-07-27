from random import randint
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
screen.colormode(255)

tim.pensize(5)
tim.speed(0)


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)


def draw_shape(angles):
    for _ in range(angles):
        tim.forward(100)
        tim.left(360/angles)   


angles = 3
while angles <= 9:
    tim.pencolor(random_color())
    draw_shape(angles)
    angles += 1























screen.exitonclick()
    
