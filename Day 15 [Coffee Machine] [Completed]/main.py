MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    """ Prints the resources available in the machine"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def ingredients(choice):
    """ Returns True if the machine have enough ingredients for the drink"""
    item_ingredients = MENU[choice]["ingredients"]
    for ingredient in item_ingredients:
        if resources[ingredient] < item_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def generate_coins():
    """Returns the total amount of money the user has"""
    coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    total_money = 0
    for coin in coins:
        amount = int(input(f"How many{coin}: "))
        value = coins[coin]
        total = amount * value
        total_money += total
    return total_money


def make_transaction(money_in_machine):
    """Checks if the user has enough money and returns True if they have and False if they don't"""
    drink_cost = MENU[user_choice]["cost"]
    dollars = generate_coins()
    if dollars >= drink_cost:
        if dollars > drink_cost:
            change = dollars - drink_cost
            print(f"Here is {change} dollars in change")
            money_in_machine += dollars
        else:
            money_in_machine += dollars
        print(f"Here is your {user_choice}. Enjoy!")
        return True
    else:
        print("Sorry that 's not enough money. Money refunded.")
        return False


def update_resources(choice):
    """Updates the resources in the machine"""
    item_ingredients = MENU[choice]["ingredients"]
    for ingredient in item_ingredients:
        resources[ingredient] -= item_ingredients[ingredient]


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso,latte/cappuccino): ")  # gets input from the user
    if user_choice == "off":  # turns off the machine
        is_on = False
    elif user_choice == "report":  # returns report of resources in the machine
        print_report()
    else:
        if ingredients(choice=user_choice):  # checks if enough ingredients are available
            if make_transaction(money_in_machine=profit):  # checks if the user has enough money
                profit += MENU[user_choice]["cost"]  # adds cost to the profit
                update_resources(choice=user_choice)  # updates the resources in the machine
