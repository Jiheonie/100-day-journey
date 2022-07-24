from base64 import encode
from string import ascii_lowercase


alphabet = list(ascii_lowercase)


def caesar(direction, text, shift):
    end_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                position = (position + shift) % 26
            if direction == "decode":
                position = (position - shift) % 26
            end_text += alphabet[position]
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}") 
