from art import logo
from modules import clear,operations

clear()
print(logo)



first_number = float(input("What is the first number: "))
for symbol in operations:
    print(symbol)

continue_calc = True

while continue_calc:
    operator = input("Pick an operation: ")
    next_number = float(input("What is the next number: "))

    calc_function = operations[operator]
    answer = calc_function(first_number, next_number)

    print(f"{first_number} {operator} {next_number} = {answer}")

    continue_message = input(f"Type 'y' to continue to calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_message == 'y':
        first_number = answer
        clear()
        print(f"Current number: {first_number}")
    else:
        continue_calc = False
