# Day 4 project - Rock-Paper-Scissors game.

# Greet the user to the game.
print("\nWelcome to Rock Paper Scissors.")
print("You will be playing against the computer.")

# Import random module.
import random

# ASCII art for rock, paper and scissors.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the available actions in a list.
actions = [rock, paper, scissors]


# Ask the user's choice.
user_choice = int(input("\nWhat do you choose? \nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    
# Get computers choice.
computer_choice = random.randint(0,2)

# Print ASCII art for both user's and computer's choice on the screen.
print(f"You chose {actions[user_choice]}")
print(f"\nComputer chose {actions[computer_choice]}")

# Check and show the result on the screen.
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
else:
    print("You win!")
