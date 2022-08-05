from turtle import Turtle, Screen
from pandas import read_csv
from state import State

screen = Screen()
map = "blank_states_img.gif"
screen.addshape(map)


# set background - bg
bg = Turtle()
bg.shape(map)


data = read_csv("50_states.csv")
all_states = data["state"].to_list()


num_of_states_guessed = 0
states_guessed = []


while len(states_guessed) < 50:
    guess = screen.textinput(title=f"{num_of_states_guessed}/50 states correct".title(), 
                            prompt="Type your answer here:").title()

    if guess == "Exit":
        break

    right_answer = guess in all_states  
    available = guess not in states_guessed

    if right_answer and available:
        state_data = data[data["state"] == guess]       #  it's mean    
                                                        #  state_data["state"].item() == guess
                                                        #  type = str
        x = int(state_data["x"])
        y = int(state_data["y"])
        state = State(x, y, guess)
        num_of_states_guessed += 1
        states_guessed.append(guess)


for state in data["state"]:
    if state in states_guessed:
        data = data.drop(data[data["state"] == state].index)

data.to_csv("learn-state.csv")



screen.exitonclick()






