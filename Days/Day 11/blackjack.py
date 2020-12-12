# Day 11 project - Blackjack.


############### Our Blackjack Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## The cards in the deck have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


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


def deal_card():
    """
    Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def get_result(user_hand, computer_hand):
    """
    Calculates and prints the final result and calls the play_game() function recursively. 
    """
    # Check if sum of computer's hand is less than 17.
    # If it is, draw more cards for computer until it crosses 17.
    while sum(computer_hand) < 17:
        computer_hand.append(deal_card())
    
    # Find final sum of cards of both user and computer.
    user_hand_sum = sum(user_hand)
    computer_hand_sum = sum(computer_hand)

    # Print the final output to the user.
    print(f"\nYour final hand was : {user_hand}")
    print(f"Your final score was : {user_hand_sum}")

    print(f"\nComputer's final hand was : {computer_hand}")
    print(f"Computer's final score was : {computer_hand_sum}")
    
    # Compare both sums and find out who won.
    if user_hand_sum == computer_hand_sum:
        print(ascii_art.draw)
    elif user_hand_sum > 21:
        print("\nIt's a bust! You crossed 21.")
        print(ascii_art.you_lose)
    elif computer_hand_sum > 21:
        print("\nIt's a bust! The computer crossed 21.")
        print(ascii_art.you_win)
    elif user_hand_sum == 21 and len(user_hand) == 2:
        print("\nYou got a blackjack.")
        print(ascii_art.you_win)
    elif computer_hand_sum == 21 and len(computer_hand) == 2:
        print("\nThe computer got a blackjack.")
        print(ascii_art.you_lose) 
    elif user_hand_sum > computer_hand_sum:
        print(ascii_art.you_win)
    else:
        print(ascii_art.you_lose)

    # Call the play_game() function recursively.
    #clear()
    play_game()


def play_game():
    """
    Main function to run the game.
    """
    # Ask the user if he wants to play a game of blackjack.
    choice = input("\nWould you like to play a game of Blackjack? (y/ n)\t")

    # Empty lists to store the user's and computer's cards.
    user_cards = []
    computer_cards = []
    # Flag to quit the game on user input.
    quit_game = False
    
    # Main while loop to keep the game running.
    while not quit_game:
        if choice == "n":
            quit_game = True
            clear()
            print(ascii_art.good_bye)
        elif choice == "y":
            clear()
            print(ascii_art.logo)
            
            # Deal 2 cards for both user and computer to start the game.
            for _ in range(2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            
            # Check if user or computer did not get 2 aces.
            # If so, change the value of an ace to 1.
            if sum(user_cards) == 22:
                user_cards.pop()
                user_cards.append(1)
            if sum(computer_cards) == 22:
                computer_cards.pop()
                computer_cards.append(1)
            
            # Flag to draw cards until user decides to pass.
            continue_drawing_card = True
            # Loop to ask user if he wants to draw one more card or not.
            while continue_drawing_card:
                print(f"\nYour cards are : {user_cards}.")
                print(f"Your current hand sum : {sum(user_cards)}")
                print(f"\nComputer's first card is {computer_cards[0]}.")
            
                draw_another_card_prompt = "\nEnter 'y' to get another card."
                draw_another_card_prompt += "\nEnter 'n' to pass.\t"            
                draw_another_card = input(draw_another_card_prompt)
                
                if draw_another_card == "n":
                    # If user chooses to pass, close the game and print the result.
                    continue_drawing_card = False
                    quit_game = True
                    get_result(user_cards, computer_cards)
                
                elif draw_another_card == "y":
                    new_card = deal_card()
                    # Check if the new card is an ace.
                    # If it is and it causes the sum to cross 21, change it's value to 1.
                    if new_card == 11 and (new_card + sum(user_cards)) > 21:
                        new_card = 1 
                    user_cards.append(new_card)
                    if sum(user_cards) >= 21:            
                        continue_drawing_card = False
                        quit_game = True
                        get_result(user_cards, computer_cards)
        else:
            quit_game = True
            clear()
            play_game()


# Call to the function to start the game.
play_game()
