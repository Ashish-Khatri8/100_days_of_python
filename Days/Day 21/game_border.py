from turtle import Turtle


class Border(Turtle):
    """A class to represent game border, inherits Turtle class."""
    def __init__(self):
        """Initialize game border."""
        super().__init__()
        self.draw_border()

    def draw_border(self):
        """Draws the game border."""
        self.hideturtle()
        self.penup()
        self.color("red")
        self.pensize(17)
        self.speed("fastest")
        self.goto(-235, 235)
        self.pendown()
        self.goto(-65, 235)
        self.penup()
        self.goto(65, 235)
        self.pendown()
        self.goto(235, 235)
        self.goto(235, -235)
        self.pendown()
        self.goto(-235, -235)
        self.goto(-235, 235)
        self.penup()
