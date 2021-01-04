# Day 21 project - Snake Game Complete.

# Import required modules.
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from game_border import Border

# Screen object settings.
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Imported class objects.
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
border = Border()

# Respond to keyboard input.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# while loop to run the game.
game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    border.draw_border()
    snake.move()
    scoreboard.display_score()

    # Detect snake-food collision.
    if snake.head.distance(food) < 16:
        scoreboard.increment_score()
        food.refresh()
        snake.create_new_segment(snake.snake_segments[-1].position())

    # Detect snake-wall collision.
    if snake.head.xcor() > 220 or snake.head.xcor() < -220 \
            or snake.head.ycor() > 220 or snake.head.ycor() < -220:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
