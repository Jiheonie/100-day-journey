from textwrap import fill
from tkinter import Button, Canvas, PhotoImage, Tk
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
cur_word = {}
dict_data = {}


def load_original_file():
    global dict_data
    words_data = pandas.read_csv('data/french_words.csv')
    dict_data = words_data.to_dict(orient='records')


def turn_not_learned_card():
    dict_data.remove(cur_word)
    to_learn_words = pandas.DataFrame(dict_data)
    to_learn_words.to_csv('data/to_learn_words.csv', index=False)
    turn_next_card()


def turn_next_card():
    global flip_timer, cur_word
    window.after_cancel(flip_timer)
    cur_word = choice(dict_data)
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=cur_word['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=cur_word['English'], fill='white')


try:
    words_data = pandas.read_csv('data/to_learn_words.csv')
except FileNotFoundError:
    load_original_file()
except pandas.errors.EmptyDataError:
    load_original_file()
else:
    dict_data = words_data.to_dict(orient='records')


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


# words field
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_img = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


# buttons
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=turn_next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0,
                      command=turn_not_learned_card)
right_button.grid(row=1, column=1)


try:
    turn_next_card()
except IndexError:
    load_original_file()
    turn_next_card()

window.mainloop()
