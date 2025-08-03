from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config( bg=THEME_COLOR, padx=20, pady=20)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        self.quiz_text = self.canvas.create_text(150,
                                                 125,
                                                 width=280,
                                                 text='Text',
                                                 font=('Arial', 20, 'italic'),
                                                 fill=THEME_COLOR)

        self.score_text = Label( text='Score: 0', font=('Arial', 20, 'italic'), bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_text.grid(column=1, row=0)

        self.true_btn = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()
    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text='You`ve reached the end of the quiz.')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)