# Day 14 project - Higher Lower game.

# Import the required modules.
import random
from os import name, system
import ascii_art
from game_data import data


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


def get_formatted_data(person):
    """
    Returns formatted data - name, description and country.
    """
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}."
    

def play_game():
    """
    Main function for the game.
    """
    choice = input("\nWould you like to play a game of Higher or Lower?\nType 'Y' or 'N'.\t")
    if choice == "N":
        clear()
        print(ascii_art.good_bye)
    elif choice != "Y":
        print("\nWrong Input!")
        play_game()
    else:
        clear()
        score = 0
        # Get first person data.
        person_1 = random.choice(data)
        
        stop_playing = False
        # while loop to keep the game running until user guesses wrong. 
        while not stop_playing:
            # Get second person's data.
            person_2 = random.choice(data)
            if person_1 == person_2:
                person_2 = random.choice(data)

            print(ascii_art.logo)
            # If user guessed right, display the score in current round.
            if score > 0:
                print(f"\nYou got it right.\nYour current score: {score}")
            
            # Get formatted data.
            print(f"\nCompare A :-\n{get_formatted_data(person_1)}")
            print(ascii_art.vs)
            print(f"\nAgainst B :-\n{get_formatted_data(person_2)}")
            
            # Prompt user for guess.
            user_choice = input("\nWho has more followers? Type 'A' or 'B'.\t")
            # Check who has more followers.
            if person_1['follower_count'] > person_2['follower_count']:
                has_more_followers = "A"
            else:
                has_more_followers = "B"
            
            # Check if the user guessed right or wrong. 
            if user_choice == has_more_followers:
                clear()
                score += 1
                # If user scores 11, user wins.
                if score == 11:
                    clear()
                    print(ascii_art.you_win)
                    stop_playing = True
                # Makes current round's person_2, the next round's person_1.
                person_1 = person_2
            else:
                clear()
                print(ascii_art.you_lose)
                print(f"You got it wrong.\nYour final score was: {score} ")
                stop_playing = True
        
        # Recursive call to the function to prompt user for playing again.
        play_game()    

# Function call to start the game.
play_game()
