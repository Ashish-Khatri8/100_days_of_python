# Day 9 project - Blind Auction.

# Import the required modules.
from os import system, name 
from ascii_art import logo

# Print the logo on the screen.
print(logo)

# Function to clear the screen after each input.
def clear(): 
    # For Windows. 
    if name == 'nt': 
        _ = system('cls') 
    # For Mac and Linux. 
    else: 
        _ = system('clear') 

# Function for calculating the highest bid.
def find_highest_bid(bidding_info):
    highest_bid = 0
    highest_bidder = ""
    
    # Find the highest bid and bidder.
    for bidder in bidding_info:
        if bidding_info[bidder] > highest_bid:
            highest_bid = bidding_info[bidder]
            highest_bidder = bidder

    # Print the name of the highest bidder and the highest bid on the screen.
    print(f"\nThe winner of the auction is: {highest_bidder}\nWith a bid of: ${highest_bid}!\n")


# Empty dictionary for storing bids.
bids = {}

# Flag for running program.
is_running = True

# Greet the user.
print("\nWelcome to the secret auction program.")

# While loop to keep the program running.
while is_running:
    # Ask user input.
    bidder_name = input("What's your name?\t")
    bid = float(input("What's your bid?\t$"))
    
    # Store each input in the dictionary as key-value pairs.
    bids[bidder_name] = bid
    
    # Ask if there are more bidders left.
    bidders_left = input("\nAre there any other bidders?\nType 'yes' or  'no'.\t")
    if bidders_left == "no":
        is_running = False
        clear()
        # Call the function to find the highest bid and print the output to the screen.
        find_highest_bid(bids)
    elif bidders_left == "yes":
        clear()
    else:
        is_running = False
        print("Wrong input!")
