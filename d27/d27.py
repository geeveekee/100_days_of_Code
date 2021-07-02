from turtle import Turtle, Screen, screensize, st
import turtle
import csv
import pandas as pd
from pandas import core

screen = Screen()
screen.title("U.S States Game")
image = "100_days_of_Code\d27\/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timmy = Turtle()
timmy.hideturtle()
timmy.pu()

#getting x and y values from map
#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)

states_data = pd.read_csv("100_days_of_Code\d27\/50_states.csv")
states_names = states_data["state"]
states_name_list = states_names.to_list()

def print_name_on_map(state_name):
    state_coo = (states_data[states_data.state == state_name])
    xcor = state_coo.iloc[0].x
    ycor = state_coo.iloc[0].y
    return xcor, ycor

correct_guess = 0
while correct_guess != 51:
    answer_state = screen.textinput(title=f"{correct_guess}/50 Ctates Correct", prompt="What's another state's name?").title()
    if answer_state in states_name_list:
        correct_guess += 1
        x, y = print_name_on_map(answer_state)
        timmy.goto(x, y)
        style = ('Courier', 10, 'italic')
        timmy.write(answer_state, font=style, align='center')
    else:
        correct_guess = correct_guess 
        
        






turtle.mainloop()




