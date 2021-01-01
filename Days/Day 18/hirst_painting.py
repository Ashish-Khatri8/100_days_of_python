# Day 18 project - Hirst Painting.

# Import required modules.
# colorgram module used here does not come packaged with Python Standard Library.
# It has to be installed with command "pip3 install colorgram.py".
import colorgram
from turtle import Turtle, Screen
from random import choice

# Extract colors from the jpeg image.
colors = colorgram.extract("image.jpeg", 35)
# Add RGB values of extracted colors as tuple in an empty list.
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# Create a Turtle() and Screen() object.
tim_turtle = Turtle()
screen = Screen()

screen.title("Hirst Painting")
# Change screen color mode to 255(For using RGB values.)
screen.colormode(255)
# Change screen window size.
screen.setup(600, 600)

# Starting coordinates for turtle object.
x = -275
y = -225

# Create a 10x10 Hirst Painting.
for row in range(10):
    tim_turtle.penup()
    tim_turtle.setx(x)
    tim_turtle.sety(y)
    for column in range(10):
        tim_turtle.forward(50)
        # Draw a circular dot of diameter 20 and a random color.
        tim_turtle.dot(20, choice(rgb_colors))
    y += 50

# Hide the turtle on painting completion.
tim_turtle.hideturtle()
screen.exitonclick()
