from turtle import Turtle, Screen
from random import randint


screen = Screen()
# screen.colormode(255)
screen.setup(800, 600)
user_guess = screen.textinput(title="Make a bet", prompt="Which color will win?")


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


turtles = []
for i in range(7):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.speed(0)
    turtle.penup()
    turtles.append(turtle)


start_x = -1 * screen.window_width() / 2 + 10
start_y = -120


# draw the final race
final_race = screen.window_width() / 2 - 30

final = Turtle()
final.hideturtle()
final.penup()
final.goto(final_race, screen.window_width() / 2)
final.pendown()
final.goto(final_race, screen.window_width() / 2 * -1)


# start
for i in range(7):
    turtles[i].goto(start_x, start_y + i * 40)


# end 
if user_guess:
    end_race = False
    while not end_race:
        for i in range(7):
            turtles[i].forward(randint(1,20))
            if turtles[i].xcor() >= final_race:
                end_race = True
                won = i
                break


    # find the winner
    won_turtle = turtles[won]
    color_winner = won_turtle.fillcolor()

    if user_guess == color_winner:
        print(f"You guessed the right winner! The {color_winner} turtle is the winner!")
    else:
        print(f"You guessed the wrong winner! The {color_winner} turtle is the winner!")
else:
    print("You didn't guess")

screen.exitonclick()