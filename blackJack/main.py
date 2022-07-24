from random import sample
from modules import clear, cards, calculate_point, hit_new_card, find_winner, set_status_deck
from art import logo


# start game
clear()

play_game = True
while play_game:
    play_signal = input("Type 'y' to play new game, 'n' to out: ")
    if play_signal == 'n':
        play_game = False
        clear()
        break
    if play_signal == 'y':
        clear()
        print(logo)

    # deck = [] is a list of card (hold the key of cards dictionary)
    my_deck = sample(list(cards), 2)    # player get 2 random cards from the deck
    dealer_deck = sample(list(cards), 2)    # dealer get 2 random cards from the deck
    # deck = ['A', 'A']  is a special situation --> At this project we will return it to Blackjack


    print(f"Your cards: {my_deck}")     # the cards player has after dealing   
    print(f"Deadler's first card: {dealer_deck[0]}")    # the first card the dealer has after dealing

    # hit a card if we need 
    should_hit = True
    while should_hit:
        hit_question = input("Type 'y' to hit another card, 'n' to stand: ")
        if hit_question == 'y':
            hit_new_card(my_deck)
            print(f"Your current deck: {my_deck}")
        else:
            should_hit = False
            print(my_deck)

    my_points = calculate_point(my_deck)

    # dealer's hit 
    dealer_hit = True
    while dealer_hit:
        dealer_points = calculate_point(dealer_deck)
        if dealer_points < 16:
            hit_new_card(dealer_deck)
        else:
            dealer_hit = False
            print(dealer_deck)


    # game's result
    # print(calculate_point(my_deck))
    print(f"Your point: {set_status_deck(my_deck)}")
    print(f"Dealer's point: {set_status_deck(dealer_deck)}")
    print(f"You {find_winner(my_deck,dealer_deck)}\n")