PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.read().splitlines()

for name in names:
    with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, name)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
        letter.write(new_letter)
