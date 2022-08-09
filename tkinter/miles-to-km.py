from telnetlib import WONT
from tkinter import Button, Entry, Tk, Label


FONT = ('Arial', 15)


def button_clicked():
    miles_number = float(input.get())
    km_number = miles_number * 1.609
    return result.config(text=km_number)


window = Tk()
window.title("Convert from miles to kilometers")
# window.minsize(width=50, height=100)
window.config(padx=20, pady=20)


# "is equal to" label
equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(row=1, column=0)


# input entry
input = Entry(width=20)
input.grid(row=0, column=1)


# result label
result = Label(text=0, font=FONT)
result.grid(row=1, column=1)


# calculate button
button = Button(text='Calculate', command=button_clicked)
button.grid(row=2, column=1)


# miles label
miles = Label(text='miles', font=FONT)
miles.grid(row=0, column=2)


# km label
km = Label(text='km', font=FONT)
km.grid(row=1, column=2)











window.mainloop()