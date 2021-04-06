# Day 55 project - Higher Lower URLs.

from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return f'<h1 style="color:red; text-align:center">Guess a number between 0 and 9.</h1>' \
           f'<img style="width:500px; height:500px; margin-left:425px" ' \
           f'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_num(guess):
    random_num = randint(0, 9)
    if guess < random_num:
        return f'<h1 style="color:red; text-align:center">Too low! Try again.</h1>' \
               f'<img style="width:500px; height:500px; margin-left:425px" ' \
               f'src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_num:
        return f'<h1 style="color:purple; text-align:center">Too high! Try again.</h1>' \
               f'<img style="width:500px; height:500px; margin-left:425px" ' \
               f'src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h1 style="color:green; text-align:center">You found me!</h1>' \
               f'<img style="width:500px; height:500px; margin-left:425px" ' \
               f'src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
