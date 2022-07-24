from random import choice
from ascii_arts import head, stages
from words import word_list
from modules import clear, no_blank



replay = True
while replay:
    clear()
    print(head)
    chosen_word = choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    display = ""
    for blank in range(word_length):
        display += "_"
    print(f"Fill in the blank with {len(chosen_word)} letters: {display}")


    while not no_blank(display) and lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess not in chosen_word:
            clear()
            print(display)
            lives -= 1
            print(stages[6 -lives])
            print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        elif guess in display:
            clear()
            print(display)
            lives -= 1
            print(stages[6 -lives])
            print(f"You guessed {guess}, that've been in the word already. You lose a life.\n")
        else:
            clear()
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display_list = list(display)
                    display_list[i] = guess
                    display = ''.join(display_list)
            print(display)
            print(stages[6 -lives])


    if no_blank(display):
        print("Congratulation! You guessed the word.\n")
    else:
        print("You are run out of lives, you lose.\n")
        print(f"The answer is {chosen_word}\n")


    replay_message = input("You want to play again? [y] for yes, [n] for no.\n").lower()
    if replay_message == "y":
        replay = True
    elif replay_message == 'n':
        replay = False
        print("Game Over.\n")
    else:
        replay = False
        print("You typed invalid word, the game will end.\n")

