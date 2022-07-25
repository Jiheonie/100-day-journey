from data import resources
from modules import clear, money, make_order

clear()

is_on = True

while is_on:
    prompt = input("What would you like? (espresso/latte/cappucino): ")
    if prompt == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Money: {money}")

    if prompt == "off":
        is_on = False
        
    if prompt == "espresso" or prompt == "latte" or prompt == "cappucino":
        money += make_order(prompt) 