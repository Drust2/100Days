from turtle import Turtle
import random
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 20/21 - Food class
"""
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.25, 0.25)
        self.color("green")
        self.speed(0)
        x0 = random.randint(-280, 280)
        y0 = random.randint(-280, 280)
        self.goto(x0, y0)
        
    def eaten(self):
        x1 = random.randint(-280, 280)
        y1 = random.randint(-280, 280)
        self.goto(x1, y1)