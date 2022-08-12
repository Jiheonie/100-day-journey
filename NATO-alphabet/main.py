
from pandas import read_csv

data = read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input('Enter your word: ').upper()
    try:
        letters_list = [phonetic_dict[c] for c in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else: 
        print(letters_list)

generate_phonetic()

