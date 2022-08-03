from turtle import Turtle, Screen


screen = Screen()


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def control(self):
        screen.listen()
        screen.onkeypress(self.go_up, "Up")

    def reach_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def start(self):
        self.goto(STARTING_POSITION)

    def crash(self, car_list):
        top = self.ycor() + 10
        bottom = self.ycor() - 10
        left = self.xcor() - 10
        right = self.xcor() + 10
        
        for car in car_list:
            collision_left = car.xcor() - 10 < left < car.xcor() + 10
            collision_right = car.xcor() - 10 < right < car.xcor() + 10
            collision_top = car.ycor() - 10 < top < car.ycor() + 10
            collision_bottom = car.ycor() - 10 < bottom < car.ycor() + 10
            if (collision_left or collision_right) and (collision_top or collision_bottom):
                return True
        return False
