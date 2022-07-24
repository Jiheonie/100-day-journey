from os import system, name
from time import sleep
from modules import caesar
from art import logo

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')



replay = True
while replay:

    clear()
    print(logo)
    direction = input("Type 'encode' to encrypt, typr 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(direction, text, shift)

    re_message = input("Type [y] to play again, type [n] to exit: ").lower()
    if re_message == 'y': 
        replay = True
    else:
        replay = False
        print("Goodbye")




