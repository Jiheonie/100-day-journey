from turtle import Turtle, Screen
from time import sleep
from snake import Snake


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()


# snake moving
is_on = True
while is_on:
    screen.update()
    sleep(0.1)

    snake.move()











screen.exitonclick()
