from turtle import Turtle


class Paddle(Turtle):
    """A class to represent the game paddle, inherits Turtle class."""
    def __init__(self, position):
        """Initialize the paddle and super class."""
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """Creates paddle and changes its attributes values."""
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("cornflower blue")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_paddle_up(self):
        """Moves the paddle up by 50 pixels."""
        if self.ycor() < 240:
            new_y = self.ycor() + 50
            self.sety(new_y)

    def move_paddle_down(self):
        """Moves the paddle down by 50 pixels."""
        if self.ycor() > -240:
            new_y = self.ycor() - 50
            self.sety(new_y)
