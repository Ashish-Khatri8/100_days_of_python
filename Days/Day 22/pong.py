# Day 22 project - Pong game.

# Use "W" and "S" keys to move the left paddle up and down respectively.
# Use "Up" and "Down" arrow keys to move the right paddle up and down respectively.
# The game ends when a player reaches a score of 7.
# The ball speed increases each time it hits a paddle, and resets after a score.

# Import required modules.
from time import sleep
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score


class Pong:
    """A class to represent the pong game."""
    def __init__(self):
        """Initialize game attributes."""
        self.screen = Screen()
        self.screen.tracer(0)
        self.game_on = True
        self.left_paddle = Paddle((-350, 0))
        self.right_paddle = Paddle((350, 0))
        self.ball = Ball()
        self.left_score = Score((-50, 250))
        self.right_score = Score((50, 250))

    def create_screen(self):
        """Create game screen."""
        # Draw a white line vertically in the mid of game screen.
        mid_line = Turtle()
        mid_line.hideturtle()
        mid_line.color("white")
        mid_line.penup()
        mid_line.goto(0, 350)
        mid_line.pendown()
        mid_line.goto(0, -350)
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        # Detect and react to keyboard input.
        self.screen.listen()
        self.screen.onkeypress(self.left_paddle.move_paddle_up, "w")
        self.screen.onkeypress(self.left_paddle.move_paddle_down, "s")
        self.screen.onkeypress(self.right_paddle.move_paddle_up, "Up")
        self.screen.onkeypress(self.right_paddle.move_paddle_down, "Down")

    def play_game(self):
        """Main method to run the game."""
        self.create_screen()
        while self.game_on:
            # Update the screen on each pass through the while loop.
            self.screen.update()
            sleep(0.07)
            # Move the ball and look for collisions.
            self.ball.move_ball()
            self.ball.detect_collisions(self.left_paddle.pos(), self.right_paddle.pos())
            # If ball has gone out of bounds, increment the score.
            if self.ball.out_of_bounds():
                if self.ball.xcor() > 0:
                    # If ball has gone out of bounds on the right side,
                    # It means that the player on left side has scored.
                    self.left_score.increment_score()
                else:
                    # If ball has gone out of bounds on the left side,
                    # It means that the player on right side has scored.
                    self.right_score.increment_score()
                # Move the ball back to center.
                self.ball.reset_position()
                sleep(0.5)
            # If a player has won(reached a score of 7), end the game.
            if self.left_score.has_won() or self.right_score.has_won():
                self.game_on = False

        self.screen.exitonclick()


# Create an object of Pong class.
pong = Pong()
# Start the game.
pong.play_game()
