cls = lambda: print("\033[2J\033[;H", end='')
cls()

from turtle import Turtle
import random
"""
Day 24 - Car
"""
class Car(Turtle):
    
    def __init__(self, x0, y0):
        super().__init__()
        self.pu()
        self.car_color()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(1, 2, 1)
        self.goto(x0, y0)
        
    def move(self, speed):
        step = self.xcor() - speed
        self.setx(step)

    def car_color(self):
        r = random.randint(0, 220)
        g = random.randint(0, 220)
        b = random.randint(0, 220)
        self.color(r, g, b)