# Day 26 project - NATO Alphabets.

# Import pandas module.
import pandas

# Read data from the csv file and store it in a dataframe.
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the dataframe using dictionary comprehension.
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# Prompt user for name.
user_input = input("\nEnter your name!\t").upper()
# Empty list to store NATO alphabets for user's name.
nato_list = []

# Loop through letters in user's name and append their NATO meanings in the list.
for letter in user_input:
    if letter in nato_alphabet_dict:
        nato_list.append(nato_alphabet_dict[letter])
    else:
        nato_list.append(letter)

# Print the final output to the user.
print(f"Your name in NATO Alphabets : \n\t{nato_list}")
