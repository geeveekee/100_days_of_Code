from turtle import Turtle, Screen, color, screensize
import turtle
import random

screen = Screen()
screen.setup(width=500, height=488)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
play_again = 'y'

while play_again == 'y':
    screen.clear()
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
    is_race_on = False

    all_turtles = []
    y = -80
    for cols in colors:
        x = -230
        t = Turtle(shape="turtle")
        t.pu()
        t.goto(x, y)
        t.color(cols)
        all_turtles.append(t)
        y += 30

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    play_again = screen.textinput(title="Congrats! You won!", prompt="Do you wanna play again?(y/n): ")
                else: 
                    play_again = screen.textinput(title=f"Oops! You lost, the winning turtle was {winning_color}", prompt="Do you wanna play again?(y/n): ")
                    if play_again == 'n':
                        screen.exit()

            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)


screen.exitonclick()
