# Day 20 project - Snake game Part 1.

# Import required modules.
from turtle import Screen
from time import sleep
from snake import Snake

# Screen object settings.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake class object.
snake = Snake()

# Listen and react to keyboard input.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# while loop to run the game.
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

screen.exitonclick()
