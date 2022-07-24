from os import system, name

def clear():
    # for windows
    _ = system('cls')

guest_dict = {}

continue_auction = True

while continue_auction:
    clear()
    name = input("What is your name? ")
    bid = int(input("How many bids? "))
    guest_dict[name] = bid

    continue_message = input("You want to continue? y/n. ").lower()
    if continue_message == 'y':
        pass #continue
    else:
        continue_auction = False

clear()

max_auction = 0
for guest in guest_dict:
    if guest_dict[guest] > max_auction:
        max_auction = guest_dict[guest]

print(max_auction)