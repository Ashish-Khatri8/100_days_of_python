from turtle import Turtle


class Ball(Turtle):
    """A class to represent the pong ball, inherits Turtle class."""
    def __init__(self):
        """Initialize the ball attributes and super class."""
        super().__init__()
        self.create_ball()
        self.vertical_direction = 1
        self.horizontal_direction = 1
        self.horizontal_speed = 15
        self.vertical_speed = 15

    def create_ball(self):
        """Creates the ball."""
        self.color("light steel blue")
        self.shape("circle")
        self.penup()
        self.speed("fastest")

    def move_ball(self):
        """Sets the ball in motion."""
        new_x = self.xcor() + (self.horizontal_speed * self.horizontal_direction)
        new_y = self.ycor() + (self.vertical_speed * self.vertical_direction)
        self.setx(new_x)
        self.sety(new_y)

    def detect_wall_collision(self):
        """
        Detects if ball has collided with upper or lower wall.
        If ball does collide, reverses its vertical direction.
        """
        if self.ycor() <= -280 or self.ycor() >= 280:
            self.vertical_direction *= -1

    def detect_right_paddle_collision(self, right_paddle_position):
        """
        Detects ball's collision with right paddle.
        If collision happens, reverses ball's horizontal direction.
        Also increases its speed.
        """
        if self.xcor() > 320 and self.distance(right_paddle_position) < 65:
            self.horizontal_direction *= -1
            self.increase_ball_speed()

    def detect_left_paddle_collision(self, left_paddle_position):
        """
        Detects ball's collision with left paddle.
        If collision happens, reverses ball's horizontal direction.
        Also increases its speed.
        """
        if self.xcor() < -320 and self.distance(left_paddle_position) < 65:
            self.horizontal_direction *= -1
            self.increase_ball_speed()

    def increase_ball_speed(self):
        """Increases ball's both vertical and horizontal speed by 2."""
        self.horizontal_speed += 2
        self.vertical_speed += 2

    def out_of_bounds(self):
        """Returns True if ball has gone out of bounds."""
        if self.xcor() > 380 or self.xcor() < -380:
            return True

    def detect_collisions(self, left_paddle_position, right_paddle_position):
        """Detects ball's collisions with walls and paddles."""
        self.detect_wall_collision()
        self.detect_left_paddle_collision(left_paddle_position)
        self.detect_right_paddle_collision(right_paddle_position)

    def reset_position(self):
        """Resets the ball after it has gone out of bounds."""
        self.goto(0, 0)
        self.horizontal_direction *= -1
        self.vertical_speed = 15
        self.horizontal_speed = 15
