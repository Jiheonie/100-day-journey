from art import logo, vs
from game_data import data
from os import system
from random import choice

def clear():
    # for windows
    _ = system('cls')

def compare_answer(compare, against):
    if compare > against:
        return "a"
    if compare < against:
        return "b"
    return "equal"

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

clear() 
print(logo)

account_b = choice(data)

still_alive = True
score = 0
while still_alive:
    account_a = account_b
    while account_b == account_a:
        account_b = choice(data)         

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    answer = compare_answer(account_a["follower_count"], account_b["follower_count"])
    guess = input('Who has more followers? Type "A" or "B": ').lower()

    if guess == answer:
        clear()
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        still_alive = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")