# Day 15 project - Coffee Machine.

# Coffee Machine menu and details.
coffee_menu = ["espresso", "latte", "cappuccino"]
coffee_details = {
    coffee_menu[0]: {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        'price': 1.50,
    },
    coffee_menu[1]: {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "price": 2.50,
    },
    coffee_menu[2]: {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "price": 3.00,
    },
}

coins_value = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# Coffee machine resources.
machine_resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100,
}


def show_menu():
    """
    Prints the menu to the user.
    """
    print('''
    ------------------------------------------------------
    What would you like?    
        Enter :-
        1 : Espresso, 2 : Latte,  3 : Cappuccino
        4 : Report,   5 : Refill, 6 : Turn machine off
    ''')


def refill_machine():
    """
    Refills the machine's resources.
    """
    machine_resources["water"] = 500
    machine_resources["milk"] = 250
    machine_resources["coffee"] = 100
    print("\tCoffee machine resources successfully refilled!")


def print_report():
    """
    Prints the report with quantity of machine resources left.
    """
    print("\n\tCoffee machine resources status:-\n")
    print(f"\t\tWater : {machine_resources['water']} ml")
    print(f"\t\tMilk : {machine_resources['milk']} ml")
    print(f"\t\tCoffee : {machine_resources['coffee']} g")


def check_machine_resources(user_choice):
    """
    Returns True if machine has enough resources to make user's coffee, otherwise False.
    """
    for resource in machine_resources:
        if machine_resources[resource] < coffee_details[user_choice][resource]:
            return False
        return True


def process_coins():
    """
    Returns total of coins inserted by user into the machine.
    """
    print("\tEnter coins :- ")
    total = int(input("\t\tQuarters :\t")) * 0.25
    total += int(input("\t\tDimes :\t\t")) * 0.10
    total += int(input("\t\tNickels :\t")) * 0.05
    total += int(input("\t\tPennies :\t")) * 0.01
    return total


def deduct_machine_resources(user_choice):
    """
    Deducts machine resources after completing user's order.
    """
    for resource in machine_resources:
        machine_resources[resource] -= coffee_details[user_choice][resource]



def make_coffee(user_choice):
    """
    Completes user's order.
    """
    # Check if machine has enough resources to complete the order.
    if not check_machine_resources(user_choice):
        print("\n\tNot enough resources!\n\tKindly refill the machine.")
    else:
        # Prompt user for inserting coins and calculate total.
        total_amount = process_coins()
        
        if total_amount < coffee_details[user_choice]["price"]:
            # If total is less than order's price, refund the money.
            print("\n\t\tSorry, that's not enough money!")
            return_amount = total_amount
        else:
            # If total is more than order's price, complete the order and return the change.
            deduct_machine_resources(user_choice)
            print(f"\n\t\tEnjoy your {user_choice.title()}.")
            return_amount = total_amount - coffee_details[user_choice]["price"]
        print(f"\t\tHere is your change : ${round(return_amount, 2)}")


def start_coffee_machine():
    """
    Starts the coffee machine.
    """
    turn_machine_off = False
    while not turn_machine_off:
        # Display the menu.
        show_menu()
        choice = input("\tYour choice :-\t")
        
        # Check for valid input.
        if not choice.isdigit() or int(choice) not in range(1, 7):
            print("\tWrong input!")
        else:
            choice = int(choice)
            if choice in range(1, 4):
                # If user has ordered any coffee, send its name as argument to make_coffee().
                make_coffee(coffee_menu[choice-1])
            elif choice == 4:
                print_report()
            elif choice == 5:
                refill_machine()
            elif choice == 6:
                turn_machine_off = True
                print("\n\tCoffee Machine turned off!")


# Function call to start the coffee machine.
start_coffee_machine()
