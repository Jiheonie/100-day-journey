from tkinter import Canvas, Tk, Label, Button
from PIL import Image, ImageTk
from math import floor


# constant
YELLOW = "#f7f5dd"
PINK = "#e2979c"
GREEN = "#9bdeac"
RED = "#e7305b"
FONT = ('Courier', 35, 'bold')
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


reps = 0
timer = None


# timer mechanism
def start_timer():
    global reps
    reps += 1
    if reps in [1,3,5,7]:
        count_down(WORK_MIN * 60)
        head_label.config(text='Work', fg=GREEN)
        checkmark_num = floor(reps / 2 + 1)
        checkmarks_list = ['✓' for _ in range(checkmark_num)]
        checkmarks_str = ''.join(checkmarks_list)
        checkmarks_label.config(text = checkmarks_str)
    if reps in [2,4,6]:
        count_down(SHORT_BREAK_MIN * 60)
        head_label.config(text='Break', fg=PINK)
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        head_label.config(text='Break', fg=RED)


# timer reset
def reset_timer():
    global reps
    head_label.config(text='Timer', fg='green')
    checkmarks_label.config(text='')
    canvas.itemconfig(canvas_text, text="00:00")
    reps = 0
    window.after_cancel(timer)



# Countdown Mechanism
def count_down(count):
    count_min = floor(count/60)
    count_sec = count % 60
    if 0 <= count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()



# UI Setup

# create Window
window = Tk()
window.title('Pomodoro')
window.config(padx=150, pady=50, bg=YELLOW)


# Create a canvas that contains the image 
canvas = Canvas(width=310, height=310, bg=YELLOW, highlightthickness=0)
# open the image
img = Image.open('tomato.png')
# resize the image smaller to fit the canvas
resized_img = img.resize((300, 300))
# conver image to tkinter
tomato_img = ImageTk.PhotoImage(resized_img)
# display the image
canvas.create_image(155, 155, image=tomato_img)
# display the remaining time
canvas_text = canvas.create_text(155, 180, text='00:00', fill="black", font=FONT)
# config paddig of canvas
canvas.grid(row=1, column=1, pady=20)


# Head Label
head_label = Label(text='Timer', fg='green', font=FONT, bg=YELLOW)
head_label.grid(row=0, column=1, pady=10)


# Start button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0, padx=30)


# Reset button
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2, padx=30)


# checkmarks list
checkmarks_label = Label(font=FONT, fg='green', bg=YELLOW)
checkmarks_label.grid(row=3, column=1)




window.mainloop()