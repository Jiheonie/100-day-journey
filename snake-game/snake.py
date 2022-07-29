from turtle import Turtle, Screen


screen = Screen()


DEFAULT_LENGTH = 3
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


positions = []
for i in range(DEFAULT_LENGTH):
    x = MOVE_DISTANCE * -i
    y = 0
    positions.append((x, y))
# => [0, -20, -40]

class Snake:
    def __init__(self):
        self.length = DEFAULT_LENGTH
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def create_snake(self):
        for position in positions:
            self.add_body(position)

    def add_body(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.speed(1)
        new_part.penup()
        new_part.goto(position)
        self.body.append(new_part)

    def extend(self):
        self.add_body(self.tail.position())
        self.length += 1

    def move(self):
        for part_num in range(self.length - 1, 0, -1):
            new_x = self.body[part_num - 1].xcor()
            new_y = self.body[part_num - 1].ycor()
            self.body[part_num].goto(new_x, new_y)
        self.control()
        self.head.forward(MOVE_DISTANCE)

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
