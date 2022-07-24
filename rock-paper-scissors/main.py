from random import randint
from rpc import check_number, play_rpc
from game_images import game_images

replay = True
while replay:
    my_choice = int(input("What do your choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))
    check = check_number(my_choice)
    if check:
        print(game_images[my_choice])
        print("Computer choice: ")
        computer_choice = randint(0,2)
        print(game_images[computer_choice])
        play_rpc(my_choice, computer_choice)

    replay_message = input("You want to play again? [Y] for Yes, [N] for No: ").lower()
    if replay_message == 'n':
        replay = False
    elif replay_message == 'y':
        replay = True
    else:
        print("You typed invalid character, the game will end!")
        replay = False
