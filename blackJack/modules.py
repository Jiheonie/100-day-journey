from os import system
from random import choice

def clear():
    # for windows
    _ = system('cls')

cards = {   # card decks
    'A': 11, 
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}   

hihi = 1

def calculate_point(deck):
    total_point = 0
    number_of_a = deck.count('A')
    for card in deck:
        total_point += cards[card]
    while total_point > 21 and number_of_a > 0:
        total_point -= 10
        number_of_a -= 1
    return total_point

def hit_new_card(deck):
    new_card = choice(list(cards))
    deck.append(new_card)
    return deck

def set_status_deck(deck):
    has_a = 'A' in deck
    if has_a == True and calculate_point(deck) == 21 and len(deck) == 2:
        return "Blackjack"
    if deck == ['A', 'A']:  # special situation 
        return "Blackjack"
    if calculate_point(deck) > 21:
        return "Out"
    return calculate_point(deck)

def find_winner(deck1, deck2):
    status1 = set_status_deck(deck1)
    status2 = set_status_deck(deck2)
    if status1 == "Blackjack" and status2 == "Blackjack":
        return "draw"
    if status1 == "Blackjack":
        return "win"
    if status2 == "Blackjack":
        return "lose"
    if status1 == "Out" and status2 == "Out":
        return "draw"
    if status1 == "Out":
        return "lose"
    if status2 == "Out":
        return "win"
    if calculate_point(deck1) == calculate_point(deck2):
        return "draw"
    if calculate_point(deck1) > calculate_point(deck2):
        return "win"
    return "lose"

