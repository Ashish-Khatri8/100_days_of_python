from turtle import Turtle


class Score(Turtle):
    """A class to represent a player's score, inherits Turtle class."""
    def __init__(self, position):
        """Initialize the score and super class."""
        super().__init__()
        self.score = 0
        self.create_score(position)

    def create_score(self, position):
        """Creates the score object with its attributes values."""
        self.hideturtle()
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.display_score()

    def display_score(self):
        """Displays the score on the screen."""
        self.clear()
        self.write(f"{self.score}", False, "center", ("Arial", 30, "bold"))

    def increment_score(self):
        """Increments the score by 1."""
        self.score += 1
        self.display_score()

    def has_won(self):
        """
        Returns True if a player reaches a score of 7.
        And updates the score on the screen.
        """
        if self.score > 6:
            self.score = "Won"
            self.display_score()
            return True
