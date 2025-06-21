from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        self.goto(STARTING_POSITION)

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def return_home(self):
        self.goto(STARTING_POSITION)
