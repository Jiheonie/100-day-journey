from turtle import Turtle, Screen
from colorgram import extract
from random import choice

color_list = extract("D:/visual/python/100-day-journey/hirst-painting/hirst_painting.jpeg", 32)

color_palette = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

screen = Screen()
screen.colormode(255)


my_tur = Turtle()
my_tur.speed(0)

my_tur.penup()

x = -250
y = -250

my_tur.setposition(x, y)

for dot_count in range(1, 101):
    ran_color = choice(color_palette)
    my_tur.dot(20, ran_color)
    if dot_count % 100 == 0:
        my_tur.hideturtle()
    if dot_count % 10 == 0:
        y += 50
        my_tur.setposition(x, y)
        continue
    my_tur.forward(50)














screen.exitonclick()