def check_number(a):
    if a not in range(3):
        print("You typed an invalid number, you lose")
        return False
    return True

def play_rpc(a, b):
    if a > b:
        print("You win")
    elif a == 0 and b == 2:
        print("You win")
    elif a < b:
        print("You lose")
    elif a == 2 and b == 0:
        print("You lose")
    else:
        print("You draw") 