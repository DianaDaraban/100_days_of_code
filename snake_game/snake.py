from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body =[]
        self.square_number = 3
        self.score = 0
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for square in range(0, self.square_number):
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(int(snake.pos()[0]) - square * 20, 0)
            self.body.append(snake)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.body.append(snake)

    def extend(self):
        self.add_segment(self.body[-1].position())


    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg - 1].xcor()
            new_y = self.body[seg - 1].ycor()
            self.body[seg].goto(new_x, new_y)
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
