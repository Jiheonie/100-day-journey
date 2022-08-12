from tkinter import END, Button, Entry, Label, PhotoImage, Tk, Canvas, messagebox
from random import randint, choice, shuffle
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

def generate_password():
    password = []
    password.extend([choice(letters) for _ in range(randint(8, 10))])
    password.extend([choice(numbers) for _ in range(randint(2, 4))])
    password.extend([choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '':
        messagebox.showerror(title='Oops', message="Please enter the website's name you want to save.") 
        return
    if password == '':
        messagebox.showerror(title='Oops', message="Please enter the password.") 
        return

    is_ok = messagebox.askokcancel(title=website, message=f'There are details entered: \nUsername: {username}\nPassword: {password}\nIs it ok to save?')

    if is_ok:
        with open('data.txt', 'a')  as data:
            data.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


# logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text='Website :')
website_label.grid(row=1, column=0)

# Username label
username_label = Label(text='Email/Username :')
username_label.grid(row=2, column=0)

# Password label
password_label = Label(text='Password :')
password_label.grid(row=3, column=0)

# website entry
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky='ew')
website_entry.focus()

# username entry
username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
username_entry.insert(0, 'hoang@gmail.com')

# password entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew')

# generate button
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

# add button
add_button = Button(text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')




window.mainloop()