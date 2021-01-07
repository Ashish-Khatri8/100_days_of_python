# Day 23 project - Turtle Crossing game.

# The player(Turtle) can only move upwards. Use "Up" arrow key to do so.
# If the player collides with any obstacle, the game ends.
# If the player reaches the finish line, a new level will start with increased game speed.

# Import required modules.
from turtle import Screen, Turtle
from time import sleep
from player import Player
from obstacles import Obstacles
from scoreboard import ScoreBoard


class TurtleCrossing:
    """A class to represent the game Turtle Crossing."""
    def __init__(self):
        """Initialize all game attributes."""
        self.stop_game = False
        self.screen = Screen()
        self.player = Player()
        self.obstacles = Obstacles()
        self.scoreboard = ScoreBoard()

    def create_screen(self):
        """Creates the game screen."""
        self.screen.tracer(0)
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("honeydew")
        self.screen.colormode(255)
        self.screen.title("Turtle Crossing")
        self.screen.listen()
        self.screen.onkey(self.player.move_up, "Up")
        # Draws the finish line on top of the screen.
        finish_line = Turtle()
        finish_line.penup()
        finish_line.hideturtle()
        finish_line.goto(-300, 260)
        finish_line.pendown()
        finish_line.goto(300, 260)

    def play_game(self):
        """Main method to run the game."""
        # Create screen, player and scoreboard.
        self.create_screen()
        self.player.create_player()
        self.scoreboard.create_scoreboard()

        # while loop to keep the game running, until it ends.
        while not self.stop_game:
            # Update screen animations after each 0.085 second.
            self.screen.update()
            sleep(0.085)
            # Display the scoreboard on the screen.
            self.scoreboard.display_scoreboard()
            # Create and move the obstacles.
            for _ in range(self.scoreboard.level):
                # If current level is x, then the create_obstacles() method will be called x times.
                self.obstacles.create_obstacles()
            self.obstacles.move_obstacles()

            # Detect player's collision with obstacles.
            if self.obstacles.detect_collision(self.player.pos()):
                self.scoreboard.game_over()
                self.stop_game = True

            # If player reached the finish line, increase game and obstacles level.
            # Also, reset the player at its starting position.
            if self.player.ycor() > 260:
                sleep(0.7)
                self.scoreboard.increase_level()
                self.obstacles.increase_obstacles_level()
                self.player.reset_player()

        # Screen should close on clicking on it after the game ends.
        self.screen.exitonclick()


# TurtleCrossing class object declaration and call to play_game() method.
turtle_crossing = TurtleCrossing()
turtle_crossing.play_game()
