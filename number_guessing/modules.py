from os import system


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def clear():
    # for windows
    _ = system('cls')

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    if difficulty == 'hard':
        return HARD_LEVEL_ATTEMPTS