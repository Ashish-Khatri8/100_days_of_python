from turtle import Turtle


class Player(Turtle):
    """A class to represent the player, inherits Turtle class."""
    def __init__(self):
        """Initialize player's starting position and super class."""
        super().__init__()
        self.starting_position = (0, -280)

    def create_player(self):
        """Creates the player."""
        self.shape("turtle")
        self.color("dark green")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.goto(self.starting_position)

    def move_up(self):
        """Moves the player up by 20 pixels on the screen."""
        self.forward(20)

    def reset_player(self):
        """Resets the player at its starting position."""
        self.goto(self.starting_position)
