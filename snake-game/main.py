from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800


width_edge = CANVAS_WIDTH / 2 - 10
height_edge = CANVAS_HEIGHT / 2 - 10


screen = Screen()
screen.bgcolor("black")
screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
screen.title("Snake Game")
screen.tracer(0)


scoreboard = Scoreboard()
snake = Snake()
food = Food()


# start
is_on = True
while is_on:
    screen.update()
    sleep(0.1)

    snake.move()

    # detect collistion with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        scoreboard.increase()

    # detect collision with the wall 
    if snake.head.xcor() > width_edge or snake.head.xcor() < -width_edge or snake.head.ycor() > height_edge or snake.head.ycor() < -height_edge:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for part in snake.body[1:]:
        # if head collides with any part of the body 
        if snake.head.distance(part) < 15:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
