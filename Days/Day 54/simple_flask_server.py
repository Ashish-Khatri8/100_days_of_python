# Day 54 project - Simple Flask Web Server.

from flask import Flask

# Creating flask app.
app = Flask(__name__)


@app.route('/')
def home_page():
    return "This is home page!"


@app.route('/hello')
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
