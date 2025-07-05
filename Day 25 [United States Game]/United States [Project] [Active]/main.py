"""
TODO - Project requirements
1. if correct state use the coordinates in the csv file to write in the canvas
2. if not correct state ask the question again
3. count the correct number of states and show it in the header
4. when the user exits, generate a csv file that lists state that haven't not been answered correctly
"""

import turtle
import pandas as pd

image = (
    "Day 25 [United States Game]/United States [Project] [Active]/blank_states_img.gif"
)
screen = turtle.Screen()
screen.title("US. States Game")
screen.addshape(image)

state_map = turtle.shape(image)

state_name = turtle.Turtle()

data = pd.read_csv(
    "Day 25 [United States Game]/United States [Project] [Active]/50_states.csv"
)
data.state = data.state.str.lower()
state_names_list = data.state.tolist()


def write_state_name(inputted_state_name):
    x = data.x[data.state == inputted_state_name.lower()].values[0]
    y = data.y[data.state == inputted_state_name.lower()].values[0]

    state_name.hideturtle()
    state_name.penup()
    state_name.setx(x)
    state_name.sety(y)
    state_name.pendown()
    state_name.pendown()
    state_name.write(answer_state.title())


correct_states = []
missed_states = []
while len(correct_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(correct_states)} / {len(state_names_list)} States Correct ",
        prompt="What's another states name",
    ).lower()

    if answer_state.lower() == "exit":

        missed_states = [state for state in state_names_list if state not in correct_states]
        data = {"States to learn": missed_states}
        df = pd.DataFrame(data)
        df.to_csv(
            "Day 25 [United States Game]/United States [Project] [Active]/States to learn.csv",
            index=False,)
        print("A file has been saved")
        break

    if answer_state in state_names_list:
        write_state_name(answer_state)
        correct_states.append(answer_state)
