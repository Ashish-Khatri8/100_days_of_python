from turtle import Turtle


class ScoreBoard(Turtle):
    """A class to represent the game scoreboard, inherits Turtle class."""
    def __init__(self):
        """Initialize game score and Turtle class attributes and methods."""
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("cornflower blue")
        self.speed("fastest")
        self.goto(0, 225)

    def display_score(self):
        """Displays score on screen."""
        self.clear()
        self.write(f"Score : {self.score}", False, "center", ("Arial", 16, "bold"))

    def increment_score(self):
        """Increments the score by 1."""
        self.score += 1

    def game_over(self):
        """Prints game over on screen."""
        self.goto(0, 0)
        self.write("GAME OVER !", False, "center", ("Arial", 30, "bold"))
