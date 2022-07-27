from random import randint
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.title("Welcome to the turtle zoo!")
screen.colormode(255)

tim.shape("classic")
tim.pensize(1)
tim.speed(0)


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)



num_of_circles = 0

while num_of_circles < 100:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 360/100)
    num_of_circles += 1


















screen.exitonclick()
    
