from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=600)


def create_title():
    title = Turtle()
    title.color('orange red')
    title.speed(30)
    title.hideturtle()
    title.penup()
    title.setpos(-150.00, 250.00)
    title.write('Welcome to turtle race', move=False, align='left', font=('Courier New', 25, 'bold'))


def final_results(first_winner, user_input):
    result = Turtle()
    result.penup()
    result.hideturtle()
    result.setpos(-300.00, -150.00)
    if first_winner.lower() == user_input.lower():
        result.write(f" You win, the {first_winner} turtle is the winner!", move=False, align='left', font=('Courier '
                                                                                                            'New',
                                                                                                            12, 'bold'))
    else:
        result.write(f" You lose, the {first_winner} turtle is the winner!", move=False, align='left', font=('Courier '
                                                                                                             'New',
                                                                                                             12,
                                                                                                             'bold'))


def create_finishline():
    finish_line = Turtle()
    finish_line.speed(50)
    finish_line.color('lime green')
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setpos(270.00, 220.00)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.width(6)
    finish_line.fd(300)


colors = ['wheat', 'sienna', 'lime green', 'coral']


def create_turtles():
    turtles_list = []
    color_position = 0
    x = 0.00
    y = 0.00
    for number in range(4):
        each_turtle = Turtle(shape='turtle')
        each_turtle.penup()
        each_turtle.color(colors[color_position])
        each_turtle.setpos(x - 300, y)
        y += 50
        turtles_list.append(each_turtle)
        color_position += 1
    return turtles_list


user_choice = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color (Wheat / Sienna / Lime "
                                                "Green / Coral): ")
create_title()
create_finishline()
turtles = create_turtles()
speed = [0, 1, 2, 3, 4, 5]
winner = ''
crossed_final_line = False
while not crossed_final_line:
    for turtle in turtles:
        turtle.fd(random.choice(speed))
        if turtle.xcor() > 250.00:
            crossed_final_line = True
            winner = colors[turtles.index(turtle)]
final_results(winner, user_choice)
screen.listen()
screen.exitonclick()
