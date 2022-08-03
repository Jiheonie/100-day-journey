from random import choice, randint
from turtle import Turtle, speed


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2



class CarManager:
    def __init__(self) -> None:
        self.car_list = []       
        self.crash = False
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Car(self.speed)
        self.car_list.append(new_car)
        

    def move(self):
        for car in self.car_list:
            car.move()

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        for car in self.car_list:
            car.speed = self.speed


class Car(Turtle):
    def __init__(self, speed) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.speed = speed
        self.penup()
        self.setheading(180)
        rand_color = choice(COLORS)
        self.color(rand_color)
        rand_y = randint(-240, 240)
        self.goto(300, rand_y)

    def move(self):
        self.forward(self.speed)