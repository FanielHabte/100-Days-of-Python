from turtle import Turtle, Screen
import random

color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
              (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
y_position = 30.00


def create_dot():
    color = random.choice(color_list)
    tim.color(color)
    tim.forward(50)
    tim.dot(22, color)


def move_dots():
    for _ in range(10):
        create_dot()


def create_art(y):
    for _ in range(10):
        move_dots()
        tim.setpos(0.00, y)
        y += 30.00


create_art(y_position)

screen.exitonclick()
