# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from pandas import read_csv


data = read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}

word = input('Enter your word: ').upper()
letters_list = [phonetic_dict[c] for c in word]

print(letters_list)



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

