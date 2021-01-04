from turtle import Turtle
from random import randint


class Food(Turtle):
    """A class to represent snake food, inherits Turtle class."""
    def __init__(self):
        """Initialize snake food and Turtle class."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("chartreuse")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Displays snake food at new random position."""
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
