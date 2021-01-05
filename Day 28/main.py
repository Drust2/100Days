from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f6eec9"
RED = "#a20a0a"
GREEN = "#799351"
YELLOW = "#ffa36c"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_countdown = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global timer_countdown
    global reps
    window.after_cancel(timer_countdown)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():    
    global reps
    work_sec = WORK_MIN * 60
    sb_sec = SHORT_BREAK_MIN * 60
    lb_sec = LONG_BREAK_MIN * 60
    reps += 1
  
    if reps%2 > 0 and reps < 8:
        countdown(work_sec)
        title.config(text="Work time", fg=GREEN)
    elif reps%2 == 0 and reps < 8:
        countdown(sb_sec)
        title.config(text="Short break", fg=YELLOW)
    elif reps == 8:
        countdown(lb_sec)
        reps = 0
        title.config(text="Long break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t0):
    global reps
    global timer_countdown
    minutes = (math.floor(t0/60))
    seconds = (t0%60)
    if seconds < 10 and seconds > -1:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if t0 > 0:
        timer_countdown = window.after(1000, countdown, t0-1)
    else:
        work_sessions = math.floor(reps/2)
        mark = ""
        for i in range(work_sessions):
            mark += "✓"
        check_mark.config(text=mark)
        start_time()
 
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=PINK)

t0 = 10
    
# Creating the background
canvas = Canvas(width=210, height=223, bg=PINK, highlightthickness=0)
background = PhotoImage(file="tomato.png")
canvas.create_image(102, 111.5, image=background)
timer = canvas.create_text(102, 140, text="00:00", font=("Courier", 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Creating the UI
title = Label(text="Timer", bg=PINK, font=("Courier",30,"bold"), fg=GREEN)
title.grid(row=0, column=1)

start = Button(text="Start", width=8, highlightthickness=0, command=start_time)
start.grid(row=2,column=0)

reset = Button(text="Reset", width=8, highlightthickness=0, command=reset_time)
reset.grid(row=2,column=2)

check_mark = Label(text="", fg=GREEN, bg=PINK, font=("Courier",12,"bold"))
check_mark.grid(row=3,column=1)


window.mainloop()
