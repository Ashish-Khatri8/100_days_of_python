# Day 16 project - OOP Coffee Machine.
 
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like? ({options}report/refill/off):\t")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        if is_enough_ingredients:
            # If enough resources are there, ask for payment.
            is_payment_successful = money_machine.make_payment(drink.cost)
            if is_payment_successful:
                # If payment successfull, make coffee and deduct machine resources.
                coffee_maker.make_coffee(drink)
