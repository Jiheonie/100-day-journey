from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

def clear():
    # for windows
    _ = system('cls')

clear()

maker = CoffeeMaker()
money = MoneyMachine()
my_menu = Menu()

menu_length = len(my_menu.menu)


is_on = True

while is_on:
    prompt = input(f"What would you like? ({my_menu.get_items()}): ")
    
    if prompt == "report":
        maker.report()
        money.report()
        continue

    if prompt == "off":
        is_on = False
        break

    drink = my_menu.find_drink(prompt)

    # if drink is not None:
    can_make = maker.is_resource_sufficient(drink)

    # if we don't have enough resources
    if not can_make:
        continue
    
    # check if money is enough to order the drink
    enough_payment = money.make_payment(drink.cost)
    
    # if the money is not enough
    if not enough_payment:
        continue

    # After paying for the order, make the coffee
    maker.make_coffee(drink)