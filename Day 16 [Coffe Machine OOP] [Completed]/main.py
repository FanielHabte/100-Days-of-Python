from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
drinks = Menu()
money = MoneyMachine()
items = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
coffee_choices = drinks.get_items()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({coffee_choices}): ")
    items.name = user_choice
    if user_choice == 'report':
        coffee.report()
        money.report()
    elif user_choice == 'off':
        is_on = False
    else:
        item = drinks.find_drink(user_choice)
        items.name = user_choice
        if coffee.is_resource_sufficient(item) and money.make_payment(item.cost):
            coffee.make_coffee(item)
