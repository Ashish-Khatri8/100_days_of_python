from turtle import Turtle

# Game constants.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """
    A class to represent the snake.
    """
    def __init__(self):
        """
        Initialize and set the starting positions of snake segments.
        """
        self.snake_segments = []
        self._create_snake()
        self.head = self.snake_segments[0]

    def _create_snake(self):
        """
        Create the snake with 3 segments, each being a Turtle() object.
        """
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        """
        Moves all snake segments by 20 places.
        """
        for seg_no in range(len(self.snake_segments) - 1, 0, -1):
            # Move the current segment at its previous segment's position.
            new_x = self.snake_segments[seg_no - 1].xcor()
            new_y = self.snake_segments[seg_no - 1].ycor()
            self.snake_segments[seg_no].goto(new_x, new_y)
        # Move the first segment to set the whole snake in motion.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Moves the snake upwards, only if it's not moving downwards.
        """
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """
        Moves the snake downwards, only if it's not moving upwards.
        """
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """
        Moves the snake leftwards, only if it's not moving rightwards.
        """
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """
        Moves the snake rightwards, only if it's not moving leftwards.
        """
        if self.head.heading() != 180:
            self.head.setheading(0)
