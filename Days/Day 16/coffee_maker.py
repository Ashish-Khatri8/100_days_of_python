class CoffeeMaker:
    """
    Models the machine that makes the coffee.
    """
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 500,
            "coffee": 250,
        }

    def report(self):
        """
        Prints a report of all the machine resources.
        """
        print("\nMachine resources :-")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Returns True when order can be made, otherwise False .
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
                print("Kindly refill the coffee machine resources.")
        return can_make

    def make_coffee(self, order):
        """
        Deducts the required ingredients to complete order from the resources.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")

    def refill(self):
        """
        Refills machine resources.
        """
        self.resources["water"] = 1000
        self.resources["milk"] = 500
        self.resources["coffee"] = 250
        print("Coffee machine resources refilled!")
