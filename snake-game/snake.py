from turtle import Turtle, Screen


screen = Screen()


DEFAULT_LENGTH = 3
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.length = DEFAULT_LENGTH
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(self.length):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.speed(1)
            new_segment.penup()
            new_segment.setx(MOVE_DISTANCE * -1 * i)
            self.body.append(new_segment)

    def move(self):
        for seg_num in range(self.length - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.control()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def control(self):
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left, "Left")
        screen.onkey(self.right, "Right")
