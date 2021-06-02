cls = lambda: print("\033[2J\033[;H", end='')
cls()

from tkinter import *
from tkinter import Tk
"""
Day 31 - UI
"""
BG_COLOR = "#B1DDC6"
CARD_BACK = r".\images\card_back.png"
CARD_FRONT = r".\images\card_front.png"
OK_IMG = r".\images\right.png"
WRONG_IMG = r".\images\wrong.png"

# --------------------------- UI ---------------------------------------------
class Ui(Tk):
    
    def __init__(self): 
        super().__init__()
        self.title("Flash Card Project")
        self.config(padx=20, pady=20, bg=BG_COLOR)
        self.cards()
        self.buttons()
        
    def cards(self, text1="This should be a word eventually", text2="This is a language field", color="white", state=0, bg_file=CARD_BACK):
        canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
        background = PhotoImage(file=bg_file)
        canvas.create_image(400, 263, image=background)
        word = canvas.create_text(400, 263, text=text1, font=("Tahoma", 20, "bold"), fill=color)
        language = canvas.create_text(400, 150, text=text2, font=("Tahoma", 20, "bold"), fill=color)
        canvas.grid(column=0, row=0)
        
    def buttons(self):
        frame = Frame(bg = BG_COLOR)
        frame.grid(column=0, row=1)
        right_img = PhotoImage(file=OK_IMG)
        wrong_img = PhotoImage(file=WRONG_IMG)
        
        right_button = Button(frame, text="Right", image=right_img)
        right_button.grid(column=0, row=0, padx=50)
        wrong_button = Button(frame, text="Wrong", image=wrong_img)
        wrong_button.grid(column=1, row=0, padx=50)
        














