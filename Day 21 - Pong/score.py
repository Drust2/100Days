cls = lambda: print("\033[2J\033[;H", end='')
cls()
from turtle import Turtle
"""
Day 21 - Pong - Scoreboard
"""
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.background = []
        self.create()
        self.scorep1 = 0
        self.scorep2 = 0
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.pd()
        self.write(f"{self.scorep1}    |    {self.scorep2}", False, "center", font=("Courier", 50, "bold"))
    
    def score(self, player):
        self.clear()
        if player == 1:
            self.scorep1 += 1
        elif player == 2:
            self.scorep2 += 1
        self.write(f"{self.scorep1}    |    {self.scorep2}", False, "center", font=("Courier", 50, "bold"))

    def create(self):
        bkg = Turtle()
        bkg.color("white")
        bkg.resizemode("user")
        bkg.shape("square")
        bkg.shapesize(0.25, 40)
        bkg.pu()
        bkg.goto(0, 245)
        self.background.append(bkg)