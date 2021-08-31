import tkinter as tk

THEME_COLOR = "#375362"
FONT_QUESTION = ('Book Antiqua', 20, 'bold')
FONT_SCORE = ('Book Antiqua', 12, 'bold')


class QuizInterface:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('Quizzler')
		self.window.config(padx=20, pady=0, bg=THEME_COLOR)
		
		self.score_label = tk.Label(
			text=f"Score: ",
			font=FONT_SCORE,
			bg=THEME_COLOR,
			fg='white'
		)
		self.score_label.grid(column=1, row=0, pady=20)
		
		self.canvas = tk.Canvas(width=300, height=250)
		self.text = self.canvas.create_text(
			150,
			125,
			text='Text',
			font=FONT_QUESTION,
			fill=THEME_COLOR
		)
		# self.canvas.config()
		self.canvas.grid(column=0, row=1, columnspan=2)
		
		right_button_img = tk.PhotoImage(file='./images/true.png')
		right_button = tk.Button(
			image=right_button_img,
			highlightthickness=0,
			bd=0,
			activebackground=THEME_COLOR,
		)
		right_button.grid(column=0, row=2, pady=20)
		
		wrong_button_img = tk.PhotoImage(file='./images/false.png')
		wrong_button = tk.Button(
			image=wrong_button_img,
			highlightthickness=0,
			bd=0,
			activebackground=THEME_COLOR,
		)
		wrong_button.grid(column=1, row=2, pady=20)
		
		self.window.mainloop()