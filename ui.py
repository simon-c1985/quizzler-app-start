import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_QUESTION = ('Book Antiqua', 17, 'bold')
FONT_SCORE = ('Book Antiqua', 12, 'bold')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=0, bg=THEME_COLOR)

        self.score_label = tk.Label(
            text=f"Score: {self.quiz.score} ",
            font=FONT_SCORE,
            bg=THEME_COLOR,
            fg='white'
        )
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = tk.Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            text='Text',
            font=FONT_QUESTION,
            fill=THEME_COLOR,
            width=280
        )
        # self.canvas.config()
        self.canvas.grid(column=0, row=1, columnspan=2)

        right_button_img = tk.PhotoImage(file='./images/true.png')
        self.right_button = tk.Button(
            image=right_button_img,
            highlightthickness=0,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.answer_true,
        )
        self.right_button.grid(column=0, row=2, pady=20)

        wrong_button_img = tk.PhotoImage(file='./images/false.png')
        self.wrong_button = tk.Button(
            image=wrong_button_img,
            highlightthickness=0,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.answer_false,
        )
        self.wrong_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.text, text='You are reached the end of the Quiz.')
            self.wrong_button.config(state='disabled')
            self.right_button.config(state='disabled')

        # score = self.quiz.score
        # self.canvas.itemconfig(self.score_label, text=score)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
