cls = lambda: print("\033[2J\033[;H", end='')
cls()

from tkinter import *
from tkinter import messagebox
import pandas
import random
import UI
"""
Day 31 - Flash Card Project
"""
ENGLISH = "English"
GERMAN = "German"
WHITE = "white"
BLACK = "black"
timer_countdown = 3
word_index = None
BG_COLOR = "#B1DDC6"
CARD_BACK = r".\images\card_back.png"
CARD_FRONT = r".\images\card_front.png"
OK_IMG = r".\images\right.png"
WRONG_IMG = r".\images\wrong.png"
score = 0
# ---------------------------- Data Management--------------------------------------------
try:
    word_list = pandas.read_csv(r".\data\de_tolearn.csv")
except FileNotFoundError:
    messagebox.showerror(title="Fatal exception", message="There is not a list of words to read, the program will close now.")
else:
    to_learn = word_list
    
    def right_answer():
        global word_index
        global to_learn
        to_learn = to_learn.drop(index=word_index)
        change_word()
            
    def change_word(flip=0, correct=0):
        global word_index
        global timer_countdown
        global score    
          
        if flip == 0:
            word_index = random.randint(0, len(word_list)-1)
        de_word = word_list.German[word_index]
        en_word = word_list.English[word_index]
        if flip == 0:
            cards(text1=de_word, text2=GERMAN, color=WHITE, bg_file=UI.CARD_BACK)
            buttons()
            cycle(3)
        else:
            cards(text1=en_word, text2=ENGLISH, color=BLACK, bg_file=UI.CARD_FRONT)
            buttons(state=NORMAL)
    
    # ----------------------------- Flashcard Cycling------------------------------------------
    def cycle(t0):
        global timer_countdown
        timer_countdown = 3
        if t0 > 0 :
            timer_countdown = window.after(1000, cycle, t0-1)
            print(t0)
        else:
            change_word(flip=1)
            timer_countdown = 5
        
    
    # --------------------------------------- UI ----------------------------------------------
    window = Tk()
    window.title("Flash Card Project")
    window.config(padx=20, pady=20, bg=BG_COLOR)
    
    def cards(master=window, text1="This should be a word eventually", text2="This is a language field", color="white", state=0, bg_file=CARD_BACK):
        canvas = Canvas(master, width=800, height=526, bg=BG_COLOR, highlightthickness=0)
        background = PhotoImage(file=bg_file)
        canvas.create_image(400, 263, image=background)
        word = canvas.create_text(400, 263, text=text1, font=("Tahoma", 20, "bold"), fill=color)
        language = canvas.create_text(400, 150, text=text2, font=("Tahoma", 20, "bold"), fill=color)
        canvas.grid(column=0, row=0)
        
    def buttons(state=DISABLED):
        frame = Frame(bg = BG_COLOR)
        frame.grid(column=0, row=1)
        right_img = PhotoImage(file=OK_IMG)
        wrong_img = PhotoImage(file=WRONG_IMG)
        
        right_button = Button(frame, text="Right", state=state, command=right_answer)
        right_button.grid(column=0, row=0, padx=50)
        wrong_button = Button(frame, text="Wrong", state=state, command=change_word)
        wrong_button.grid(column=1, row=0, padx=50)
        

    cards()
    
    change_word()
        
    window.mainloop()
    to_learn.to_csv(r".\data\de_tolearn.csv", index=False)

