# Day 25 project - Indian States.

# Import required modules.
import pandas
import turtle

# Create the screen with the map image.
map_image = "blank_map.gif"
screen = turtle.Screen()
screen.setup(width=650, height=650)
screen.title("Indian States.")
screen.addshape(map_image)
turtle.shape(map_image)

# Read the data from csv file and create a list of all states names from it.
data = pandas.read_csv('28_states.csv')
all_states = data["state"].to_list()
# Empty list to store names of the states user guessed right.
guessed_states = []

# Turtle object attributes that will write state names on the map.
screen_text = turtle.Turtle()
screen_text.penup()
screen_text.speed("fastest")
screen_text.hideturtle()
screen_text.color('green')

# while loop to run the game.
while len(guessed_states) < 28:
    # Ask user for input.
    prompt = f"Correct guesses : {len(guessed_states)} / 28\nEnter 'Done' to exit."
    title = "Guess a state's name."
    user_input = screen.textinput(prompt=prompt, title=title).title()

    if user_input == "Done":
        break
    elif user_input in all_states and user_input not in guessed_states:
        guessed_states.append(user_input)
        state_name = data[data.state == user_input]
        x = int(state_name.x)
        y = int(state_name.y)
        if " " in user_input:
            user_input = user_input.replace(' ', "\n")
        screen_text.goto(x, y)
        screen_text.write(user_input, False, "center", ("Arial", 12, "bold"))
else:
    screen_text.color("black")
    screen_text.goto(140, 170)
    message = "You guessed them all.\nYou win!"
    screen_text.write(message, False, align="center", font=("Arial", 23, "bold"))
    screen.exitonclick()
