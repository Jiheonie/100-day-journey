from tkinter import Entry, Tk, Label, Button


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title('First GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text='I am a label')
my_label.config(text='HIhi')
my_label.grid(row=0, column=0)


# Entry
input = Entry()
print(input.get())
input.grid(row=2, column=3)


# Button
button = Button(text='Button', command=button_clicked)
button.grid(row=1, column=1)


new_button = Button(text='New Button', command=button_clicked)
new_button.grid(row=0, column=2)


window.mainloop()