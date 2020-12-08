# Day 8 project - Caesar Cipher.

# Import logo from art.py and print it.
from art import logo
print(logo)

# Store all alphabets, numbers and symbols in a list.
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
              '{', '}', '[', ']', '|', '/', ',', '.', '<', '>', '?', ';', ':', '"', "'", '\\']


# Create a function to encrypt or decrypt the input.
def caesar(input_text, shift_no, cipher_direction):
    output_text = ""
    # Get the shift_no within characters list range.
    shift_no %= 94

    if cipher_direction == "decode":
        shift_no *= -1

    # Encrypt / Decrypt iput.
    for letter in input_text:
        # Check if the letter in input is in the characters list or not.
        if letter in characters:
            # Get the letter's index in the characters list.
            position = characters.index(letter)

            # Get new position for the letter.
            if position + shift_no > 93:
                new_position = position + shift_no - 94
            elif position + shift_no < 0:
                new_position = position + shift_no + 94
            else:
                new_position = position + shift_no
            
            output_text += characters[new_position]
        else:
            output_text += letter
    
    # Print the output to the screen.
    print(f"The {cipher_direction}d text is: {output_text}")


# Flag for keeping the game running.
running = True

while running:
    # Ask for user input.
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\t").lower()
    shift = int(input("Type the shift number:\t"))

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
    else:
        print("Wrong input!")

    # Ask the user if he would like to go again.
    choice = input("\nWould you like to go again? (Yes, No)\t")
    if choice != "Yes":
        running = False
        print("Goodbye!")
