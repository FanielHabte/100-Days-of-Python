import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [-40, -100, -160, -220, 40, 100, 160, 220]
y = -40


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 250))
        self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.setx(car.xcor() - self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
