import turtle
from symtable import Class
from turtle import Turtle
import pandas as pd

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US. States Game")
screen.addshape(image)

state_map = turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another states name").lower()

data = pd.read_csv("50_states.csv")
data.state = data.state.str.lower()
state_names_list = data.state.tolist()


class States(Turtle):

    def __init__(self, x, y, state_name):
        super().__init__()
        self.create_state_names(self, x, y, state_name)

    def create_state_names(self, x, y, state_name):
        self.hideturtle()
        self.penup()
        self.setx(x)
        self.sety(y)
        self.pendown()
        self.pendown()
        self.write(state_name)


while True:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another states name").lower()
    if answer_state in state_names_list:

        coordinates_y = data.y[data.state == answer_state.lower()].values
        coordinates_x = data.x[data.state == answer_state.lower()].values

        States(Turtle,coordinates_y,coordinates_x,answer_state)

        output_state_name = data.state.str.title()

    screen.exitonclick()
