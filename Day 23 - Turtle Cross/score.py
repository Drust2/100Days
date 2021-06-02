cls = lambda: print("\033[2J\033[;H", end='')
cls()

from turtle import Turtle
"""
Day 23 - Score class
"""
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 280)
        self.score = 0
        self.pd()
        self.write(f"Level: {self.score}", False, "left", ("Courier", 13, "bold"))
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, "left", ("Courier", 13, "bold"))
        
    def game_over(self):
        self.pu()
        self.goto(0,0)
        self.pd()
        self.write("GAME OVER", False, "Center", ("Courier", 26, "bold"))

