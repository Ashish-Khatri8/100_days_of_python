# Day 5 project - Password Generator.

# Import the random module.
import random

# Create separate lists for letters, numbers and symbols. 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '|', '_', '@', '^']

# Greet the user.
print("\nWelcome to the Password Generator!")

# Ask user input.
no_letters= int(input("\nHow many letters would you like in your password?\t")) 
no_symbols = int(input(f"How many symbols would you like in your password?\t"))
no_numbers = int(input(f"How many numbers would you like in your password?\t"))

# Empty list to hold password.
password_list = []

# Create password.
for letter in range(0, no_letters):
    letter = random.choice(letters)
    password_list.append(letter)

for symbol in range(0, no_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)

for number in range(0, no_numbers):
    number = random.choice(numbers)
    password_list.append(number)

# Shuffle the password list.
random.shuffle(password_list)

# Create an empty string to store the password.
password = ""

# Add elements from password_list to password string.
for element in password_list:
    password += element

# Print the output on the screen.
print(f"\nYour password is:\t{password}\n")
