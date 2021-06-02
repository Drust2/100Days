cls = lambda: print("\033[2J\033[;H", end='')
cls()
from turtle import Turtle
"""
Day 21 - Debug stats
"""
class Stats(Turtle):
    
    def __init__(self):
        super().__init__()
        self.xcoord = 0
        self.ycoord = 0
        self.pu()
        self.goto(350, -290)
        self.color("white")
        self.hideturtle()
        self.pd()
        
    
    def tracking(self):
        self.clear()
        self.write(f"x: {self.xcoord} | y: {self.ycoord}", False, "center", font=("Tahoma", 7, "bold"))

