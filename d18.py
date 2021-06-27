from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_for():
    timmy.forward(10)

def move_back():
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading) 

def clear():
    timmy.clear()
    timmy.pu()
    timmy.home()
    timmy.pd()

screen.listen()
screen.onkey(move_for, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()