from data import resources, MENU
from modules import clear, money, make_order

clear()

still_active = True

while still_active:
    prompt = input("What would you like? (espresso/latte/cappucino): ")
    if prompt == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Money: {money}")

    if prompt == "off":
        still_active = False
        
    if prompt == "espresso" or prompt == "latte" or prompt == "cappucino":
        money += make_order(prompt)