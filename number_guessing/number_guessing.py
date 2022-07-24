from random import randint
from art import logo
from modules import clear, set_difficulty


clear()
print(logo)
print("Welcome to guessing game")
print("I'm thinking of a number between 1 and 100")
number_needed = randint(1, 100)

attempts = set_difficulty()

while attempts > 0:
    print(f"You have {attempts} attempts to guess the number.")
    guessing_number = int(input("Make a guess: "))
    if guessing_number > number_needed:
        print("Too high")
        attempts -= 1
    if guessing_number < number_needed:
        print("Too low")
        attempts -= 1
    if guessing_number == number_needed:
        print(f"You got it! The answer is {number_needed}.")
        attempts = -1
    if attempts > 0:
        print("Guess again")
        

if attempts == 0:
    print(f"You lost. The number is {number_needed}")