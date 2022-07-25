from os import system
from data import COINS, MENU, resources

def clear():
    # for windows
    _ = system('cls') 


# list of values of coins [0.25, 0.1, 0.05, 0.01]
coin_values = []
for item in COINS:
    coin_values.append(COINS[item]) 


def calculate_money(coin_paid):
    total = 0
    for i in range(len(coin_paid)):
        total += coin_paid[i] * coin_values[i]
    return round(total, 2)


def is_resource_sufficient(ingredients):
    is_enough = True
    missing_thing = ""
    for type in ingredients:
        if ingredients[type]  > resources[type]:
            is_enough = False
            missing_thing = type
            print(f"Sorry, there is not enough {missing_thing}.")
    return is_enough
    # return if we have enough resources for the order


def process_coin():
    print("Please insert coins.")    
    coin_paid = []
    for coin_type in COINS:
        coin_paid.append(int(input(f"How many {coin_type}s: ")))
    return calculate_money(coin_paid)
    # return the total calculated from coins inserted
    

money = 0


# When the user chose the drink
# prompt = espresso, latte, cappucino
def make_order(drink):
    order = MENU[f"{drink}"]

    # calculate resources needed 
    ingredients = order["ingredients"]

    # check if we have enough resources
    can_make = is_resource_sufficient(ingredients)

    # if we don't have enough resources
    if not can_make:
        return 0

    # if we have enough resources to make the order
    # can_make = True
    for type in ingredients:
        resources[type] -= ingredients[type]

    # cost of order
    cost = order ["cost"]

    # calculate money
    payment = process_coin()

    # check if the money is enough
    can_buy = True
    if payment < cost:
        can_buy = False

    # paid not enough money
    if not can_buy:
        print("Sorry, that's not enough money. Money refunded.")
        return 0

    # if paid enough money, now you can have your drink
    # can_buy = True
    #calculate change
    change = payment - cost 
    print(f"Here is ${change} in change")
    print(f"Here is your {drink} ☕. Enjoy!")
    return cost