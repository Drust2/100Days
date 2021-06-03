from tkinter import *
from tkinter import Tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_IMAGE = r"D:\Python Scripts\100days\Day 34 - Quiz App\images\true.png"
WRONG_IMAGE = r".\images\false.png"

class Ui(Tk):
    
    def __init__(self, quiz: QuizBrain):
        super().__init__()
        self.quiz = quiz
        self.config(padx=100, pady=20, bg=THEME_COLOR)
        self.title("Quizzler")
        self.score = 0
        self.question = "Here goes a preloaded question"
        self.resizable(False, False)
        self.score_label()
        self.question_frame()
        
        self.true_img = PhotoImage(file=RIGHT_IMAGE)
        self.false_img = PhotoImage(file=WRONG_IMAGE)
        self.buttons()
        self.next_question()
        self.mainloop()

        
    def score_label(self):
        score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", padx=100, pady=20, font=("Tahoma", 10))
        score.grid(row=0, column=0, sticky="ne")
    
    def question_frame(self):
        q_frame = Frame(bg="white")
        q_frame.grid(row=1, column=0, pady=200)
        question = Label(master=q_frame, text=self.question, width=70, height=5, fg=THEME_COLOR, bg="white", wraplength=600, font=("Tahoma", 14))
        question.pack()
    
    def buttons(self):
        photor = self.true_img
        photow = self.false_img
        b_frame = Frame(bg=THEME_COLOR)
        b_frame.grid(row=2, column=0)
        r_button = Button(b_frame, image=photor, highlightthickness=0, command=self.answer_true)
        r_button.grid(row=0, column=0, padx=50)
        w_button = Button(b_frame, image=photow, highlightthickness=0, command=self.answer_false)
        w_button.grid(row=0, column=1, padx=50)
        
    def next_question(self):
        q_text = self.quiz.next_question()
        self.question = q_text
        self.question_frame()
        
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, answer:bool):
        if answer:
            self.score += 1
            self.score_label()
            self.next_question()
        else:
            self.next_question()
        

