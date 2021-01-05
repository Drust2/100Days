cls = lambda: print("\033[2J\033[;H", end='')
cls()

from turtle import Turtle
"""
Day 23 - Frog class
"""
class Frog(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black", "green")
        self.pu()
        self.x0 = 0
        self.y0 = -280
        self.goto(self.x0, self.y0)
        self.setheading(90)

    def move(self):
        step = self.ycor() + 20
        self.goto(0, step)
    