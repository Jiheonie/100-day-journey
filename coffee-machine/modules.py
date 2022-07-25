from os import system
from data import coins, MENU, resources

def clear():
    # for windows
    _ = system('cls') 

# list of values of coins [0.25, 0.1, 0.05, 0.01]
coin_values = []
for item in coins:
    coin_values.append(coins[item]) 

def calculate_money(coin_paid):
    total = 0
    for i in range(len(coin_paid)):
        total += coin_paid[i] * coin_values[i]
    return round(total, 2)


money = 0

# When the user chose the drink
# prompt = espresso, latte, cappucino
def make_order(drink):
    order = MENU[f"{drink}"]

    # calculate resources needed 
    ingredients = order["ingredients"]
    can_make = True
    missing_thing = ""
    for type in ingredients:
        if ingredients[type]  > resources[type]:
            can_make = False
            missing_thing = type
            break

    # if we don't have enough resources
    if not can_make:
        print(f"Sorry, there is not enough {missing_thing}.")
        return 0

    # if we have enough resources to make the order
    # can_make = True
    for type in ingredients:
        resources[type] -= ingredients[type]

    # cost of order
    cost = order ["cost"]

    # calculate money
    print("Please insert coins.")    
    coin_paid = []
    for coin_type in coins:
        coin_paid.append(int(input(f"How many {coin_type}s: ")))
    money_paid = calculate_money(coin_paid)

    # the money is enough
    can_buy = True
    if money_paid < cost:
        can_buy = False

    # paid not enough money
    if not can_buy:
        print("Sorry, that's not enough money. Money refunded.")
        return 0

    # if paid enough money, now you can have your drink
    #calculate change
    change = money_paid - cost 
    print(f"Here is ${change} in change")
    print(f"Here is your {drink}. Enjoy!")
    return cost