# Day 12 project - Guess the number!

# Import the required modules.
import random
from os import name, system
import ascii_art


def clear():
    """
    Clears the output screen.
    """ 
    # For Windows. 
    if name == 'nt': 
        _ = system('cls') 
    # For Mac and Linux. 
    else: 
        _ = system('clear')


def generate_random_number():
    """
    Returns a random number between 1 and 100 (both included).
    """
    return random.randint(1, 100)


def guess_the_no():
    """
    Main function to run the program.
    """
    would_play = input("\nWould you like to play the number guessing game?\nEnter 'yes' or 'no'.\t\t")
    if would_play == "yes":
        clear()
        # Greet the user.
        print(ascii_art.logo)
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")
        
        # Get a randomly guessed number.
        random_number = generate_random_number()
        # Prompt user for difficulty level.
        get_difficulty_level = "\nChoose a difficulty level!"
        get_difficulty_level += "\nEnter:-\n\t0 for Easy\n\t1 for Medium\n\t2 for Hard\t\t"
        difficulty_level = input(get_difficulty_level)

        # Lists storing no of lives and difficulty levels.
        lives = [13, 9, 5]
        difficulty_levels = ["0", "1", "2"]

        if difficulty_level in difficulty_levels:
            lives_left = lives[int(difficulty_level)]
            print(f"You have {lives_left} lives.")
            
            continue_guessing = True
            # while loop to let user continue guessing the number, 
            # until the user has guessed correctly or run out of lives.
            while continue_guessing:
                no_guessed = int(input("\nGuess the number :-\t"))                  
                if no_guessed not in range(1, 101):
                    continue_guessing = False
                    print("Wrong Input!")
                elif no_guessed == random_number:
                    continue_guessing = False
                    print(f"\nYou guessed the number {no_guessed}!")
                    print(f"You had {lives_left} lives left!")
                    print(ascii_art.you_win)
                else:
                    # Reduce a life for each wrong guess.
                    lives_left -= 1
                    if lives_left == 0:
                        continue_guessing = False
                        print(f"\nThe number was {random_number}\nYou lost all lives!")
                        print(ascii_art.you_lose)
                    elif no_guessed > random_number:
                        print(f"Too high.\nYou have {lives_left} lives left.")
                    else:
                        print(f"Too low.\nYou have {lives_left} lives left.")
            
            # Function call to prompt user for playing again after end of while loop.
            guess_the_no()
        else:
            print("\nWrong input!")
            guess_the_no()

    elif would_play == "no":
        clear()
        print(ascii_art.good_bye)
    else:
        print("\nWrong input!")
        guess_the_no()

# Function call to start the program.
guess_the_no()
