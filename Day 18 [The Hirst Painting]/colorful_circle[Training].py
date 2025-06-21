from turtle import Turtle, Screen
import random

# while True:
#     timmy.right(90)
#     timmy.forward(100)
#     if abs(timmy.pos()) < 1:
#         break

# for x in range(15):
#     if x % 2 == 0:
#         timmy.pencolor('black')
#         timmy.forward(10)
#     else:
#         timmy.pencolor('white')
#         timmy.forward(10)


# colors = ['blue', 'green', 'red', 'purple', 'cyan1', 'brown2', 'DarkMagenta']
# number_of_side = 3
# number_of_objects = 0
#
#
# def color_choice(color_list):
#     return random.choice(color_list)
#
#
# def timmy_move():
#     timmy.right(angle)
#     timmy.forward(100)
#
#
# def update(sides, objects):
#     sides += 1
#     objects += 1
#     return sides, objects
#
#
# while number_of_objects != 10:
#     angle = 360 / number_of_side
#     timmy_move()
#     if abs(timmy.pos()) < 1:
#         timmy.pencolor(color_choice(colors))
#         number_of_side, number_of_objects = update(number_of_side, number_of_objects)

Screen().colormode(255)
# timmy.shapesize(1)
# timmy.width(15)
# timmy.speed(15)
# angles = [0, 90, 180, 270, 360]
# colors = ['linen', 'light salmon', 'burlywood', 'yellow green', 'cadet blue', 'gainsboro', 'thistle']
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(angles))

timmy = Turtle()
timmy.shape("circle")
timmy.shapesize(0.01)
timmy.speed(15)


def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    color = (r, g, b,)
    return color


for _ in range(75):
    timmy.circle(100)
    timmy.color(random_color())
    timmy.left(5)

# if abs(timmy.pos()) < 1
screen = Screen()
screen.exitonclick()
