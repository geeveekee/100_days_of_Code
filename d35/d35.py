from flask import Flask
import random
random_number = random.randint(1, 10)


app = Flask(__name__)

@app.route('/')
def home_page():
    return "<div><h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img></div>"

@app.route("/<int:number>")
def guessed_number(number):
    if number > random_number:
        return "<h1>Too High, Try Again!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif int(number) < random_number:
        return "<h1>Too Low, Try Again!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    else:
        return "<h1>You found Me!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
        