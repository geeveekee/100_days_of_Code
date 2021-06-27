import turtle
import colorgram as cg
from turtle import Turtle, Screen
import random
#To get list of colors from out given image
""" colors = cg.extract('100_days_of_Code\d17\img.jpg', 20)
cols_list = []
for cols in colors:
    col = (cols.rgb.r, cols.rgb.g, cols.rgb.b)
    print(col)
    cols_list.append(col) """


color_list = [(229, 249, 73), (229, 237, 253), (67, 252, 194), (17, 184, 82), (19, 15, 96), (218, 153, 94), (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203), (28, 245, 41), (248, 21, 135), (168, 3, 123), (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243)]

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
timmy.hideturtle()
timmy.pu()
turtle.colormode(255) #sets it to rgb
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def draw_circle():
    dot_col = random.choice(color_list)
    timmy.dot(20, dot_col)
    timmy.pu()
    timmy.forward(50)
    timmy.pd()
    
for y in range(0, 10):
    for x in range(0, 10):
        draw_circle()

    timmy.pu()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(50)

    for x in range(0, 10):
        draw_circle()

    timmy.pu()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(360)
    timmy.forward(50)







screen.exitonclick()