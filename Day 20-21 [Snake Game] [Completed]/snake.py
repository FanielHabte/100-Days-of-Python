from turtle import Turtle

move_distance = 10
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.x = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_seg = self.segments[-1]
        self.seg_x_cor = 0
        self.seg_y_cor = 0

    def create_snake(self):
        for number_of_turtles in range(3):
            self.add_segment()
            self.x -= 20

    def add_segment(self):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.setx(self.x)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.setpos(self.last_seg.pos())
        self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[seg_num - 1].xcor()
            new_y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_pos, new_y_pos)
        self.segments[0].fd(move_distance)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(up)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(down)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(left)

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(right)


