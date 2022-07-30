from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


scoreboard = Scoreboard()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_paddle.control("Up", "Down")
l_paddle.control("w", "s")


ball = Ball()

while True:
    screen.update()
    sleep(ball.move_speed)

    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall() 

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_paddle()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()

    # detect when right paddle miss
    if ball.xcor() > 400:
        ball.miss("right")
        scoreboard.l_score += 1

    # detect when left paddle miss
    if ball.xcor() < -400:
        ball.miss("left")
        scoreboard.r_score += 1

    scoreboard.update()


# screen.exitonclick()