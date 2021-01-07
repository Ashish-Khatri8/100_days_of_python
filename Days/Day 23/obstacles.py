from turtle import Turtle
from random import randint, choice


class Obstacles:
    """A class to represent all the obstacles in the game."""
    def __init__(self):
        """Initialize obstacles attributes."""
        self.all_obstacles = []
        self.moving_speed = 10
        # Screen y-coordinate ranges in which obstacles will move leftwards.
        self.left_moving_segments = [(-250, -200), (-150, -100), (-50, 0),
                                     (50, 100), (150, 200)]
        # Screen y-coordinate ranges in which obstacles will move rightwards.
        self.right_moving_segments = [(-200, -150), (-100, -50), (0, 50),
                                      (100, 150), (200, 250)]

    def create_obstacles(self):
        """Randomly creates an obstacle and adds it to all_obstacles list."""
        # 33% chance of an obstacle getting created when method is called.
        make_new_obstacle = randint(1, 6)
        if make_new_obstacle % 3 == 0:
            # Get a random RGB color value.
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            random_color = (r, g, b)
            # New obstacle attributes.
            new_obstacle = Turtle(shape="arrow")
            new_obstacle.speed("fastest")
            new_obstacle.penup()
            new_obstacle.shapesize(stretch_len=2, stretch_wid=0.9)
            new_obstacle.color(random_color)

            # if direction is 0, obstacle will move leftwards, otherwise rightwards.
            direction = randint(0, 1)
            if direction == 0:
                new_obstacle.setheading(180)
                range_y = choice(self.left_moving_segments)
                random_y = randint(range_y[0], range_y[1])
                random_x = randint(250, 350)
                new_obstacle.goto(random_x, random_y)
                self.all_obstacles.append(new_obstacle)
            else:
                range_y = choice(self.right_moving_segments)
                random_x = randint(250, 350)
                random_y = randint(range_y[0], range_y[1])
                # Negative x coordinate as this obstacle will move rightwards.
                new_obstacle.goto(-random_x, random_y)
                self.all_obstacles.append(new_obstacle)

    def move_obstacles(self):
        """Moves all the obstacles in their respective directions on the screen."""
        for each_obstacle in self.all_obstacles:
            each_obstacle.forward(self.moving_speed)

    def detect_collision(self, player_position):
        """Returns True if any obstacle has collided with the player."""
        for any_obstacle in self.all_obstacles:
            if any_obstacle.distance(player_position) < 19:
                return True

    def increase_obstacles_level(self):
        """
        Increases moving speed of all obstacles by 3.
        """
        self.moving_speed += 3
