# Day 10 project - Calculator.

# Import the required modules.
from os import system, name
from ascii_art import logo

# Function to clear the screen for new calculation.
def clear(): 
    # For Windows. 
    if name == 'nt': 
        _ = system('cls') 
    # For Mac and Linux. 
    else: 
        _ = system('clear') 

# Functions to do calculations.
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Dictionary to store available operations.
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# Function calculator.
def calculator():
    # Print the logo imported from ascii_art.py.
    print(logo)    
    
    # Flag for stopping the program.
    should_stop = False
    
    # Prompt the user for the first number.
    number_1 = float(input("Enter the first number :\t"))

    # while loop to keep the program running until user wants to exit.
    while not should_stop:
        print("\nAvailable operations are :-")
        for operation in operations:
            print(f"\t\t{operation}")
        operation_to_do = input("Enter an operation from above.\t")

        if operation_to_do not in operations:
            # Stop the calculation and restart the program.
            should_stop = True
            clear()
            print("\nInvalid input!")
            calculator()
        
        else:
            # Prompt the user for the next number.
            number_2 = float(input("Enter the next number :\t"))
            
            # Call the appropriate function in response to user input.
            function = operations[operation_to_do]
            result = round(function(number_1, number_2), 2)
            
            # Print the output to the user.
            print(f"\n{number_1} {operation_to_do} {number_2} = {result}")

        # Prompt for user input.
        prompt = f"\nType '1' to continue with {result}.\n"
        prompt += "Type '2' to start a new calculation.\n"
        prompt += "Type '0' to exit!\t"
        choice = input(prompt)

        # Act in accordance with the user input.
        if choice == "1":
            # Set number_1 to result of previous calculation.
            number_1 = result
        
        elif choice == "2":
            # Stop the ongoing calculation, clear the screen and start a new calculation.
            should_stop = True
            clear()
            # Call the calculator function recursively.
            calculator()
        
        elif choice == "0":
            # Exit the program.
            should_stop = True
            print("\nGoodBye!\n")
        
        else:
            should_stop = True
            print("Wrong input!")

# Call to calculator() function to start the program.
calculator()
