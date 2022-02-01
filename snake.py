from turtle import Turtle
STARTING_POSITONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.squares = []
        self.construct_snake()
        self.head = self.squares[0]

    def construct_snake(self):
        for positions in STARTING_POSITONS:
            self.add_square(positions)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.squares.append(new_square)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)