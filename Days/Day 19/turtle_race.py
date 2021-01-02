# Day 19 project - Turtle Race.

# Import required modules.
from turtle import Turtle, Screen
from random import randint

# Screen object settings.
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=500)


def create_turtles():
    """
    Returns a list of Turtle class objects with different colors.
    """
    turtles_list = []
    turtle_colors = ["red", "orange", "blue", "green", "purple", "black"]
    for turtle_color in turtle_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_color)
        turtles_list.append(new_turtle)
    return turtles_list


def position_turtles(turtles_list):
    """
    Positions all the turtles at their starting positions for the race.
    """
    x = -210
    y = -210
    for each_turtle in turtles_list:
        each_turtle.penup()
        each_turtle.turtlesize(2, 2)
        each_turtle.setx(x)
        each_turtle.sety(y)
        y += 80


def turtle_race(turtles_list):
    """
    Starts the turtles race and returns the color of winning turtle.
    """
    while True:
        for each_turtle in turtles_list:
            # Stop the race and return the turtle's color that won.
            if each_turtle.xcor() > 200:
                return each_turtle.pencolor()
            steps = randint(1, 7)
            each_turtle.forward(steps)


def get_result(users_turtle, winning_turtle):
    """
    Prints the final result of the race.
    """
    if users_turtle == winning_turtle:
        result = "won"
    else:
        result = "lost"
    print(f"\nYou {result}!\nThe {winning_turtle} turtle won the race.")


# Prompt user to guess which turtle wil win.
input_screen_title = "Which turtle would win?"
input_prompt = "Enter you choice.\n(red, orange, blue, green, purple, black)"
user_choice = screen.textinput(input_screen_title, input_prompt)

while not user_choice:
    user_choice = screen.textinput(input_screen_title, input_prompt)
else:
    turtles = create_turtles()
    position_turtles(turtles)
    winner = turtle_race(turtles)
    get_result(user_choice, winner)


screen.exitonclick()
