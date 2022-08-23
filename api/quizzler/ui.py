from tkinter import Canvas, Button, Label, Tk, PhotoImage
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ('Ariel', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title('Quizzler')
        self.create_label(row=0, column=1)
        self.create_canvas(row=1, column=0)
        true_image = PhotoImage(file=f'images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.enter_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file=f'images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.enter_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.window.mainloop()

    def create_label(self, row, column):
        self.score = 0
        self.label = Label(text=f'Score: {self.score}', font=FONT, bg=THEME_COLOR)
        self.label.grid(row=row, column=column,pady=20)

    def create_canvas(self, row, column):
        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, width=280, font=FONT)
        self.get_next_question()
        self.canvas.grid(row=row, column=column, columnspan=2, padx=20, pady=20)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text='You\'ve reached the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def enter_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)
    
    def enter_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.label.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')
