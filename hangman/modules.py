from os import name,system

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def no_blank(display):
    if "_" in display:
        return False
    return True



