from turtle import Turtle


class ScoreBoard(Turtle):
    """A class to represent the game scoreboard, inherits Turtle class."""
    def __init__(self):
        """Initialize level and super class."""
        super().__init__()
        self.level = 1

    def create_scoreboard(self):
        """Creates the scoreboard."""
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.goto(-230, 260)

    def display_scoreboard(self):
        """Displays the scoreboard on the screen."""
        self.clear()
        self.write(f"Level : {self.level}", False, "center", ("Arial", 20, "bold"))

    def increase_level(self):
        """Increases the level by 1."""
        self.level += 1
        self.display_scoreboard()

    def game_over(self):
        """Prints GAME OVER ! on the screen."""
        self.goto(0, 0)
        self.write(f"GAME OVER !", False, "center", ("Arial", 40, "bold"))
