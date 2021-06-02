cls = lambda: print("\033[2J\033[;H", end='')
cls()
from turtle import Turtle
import random
"""
Day 21 - Pong - Ball class
"""
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.speed(1)
        self.sety(-75)
        self.x0_speed = 3*random.choice([-1, 1])
        self.y0_speed = 5*random.choice([-1, 1])
        self.y_speed = self.y0_speed
        self.x_speed = self.x0_speed

    def bounce_walls(self):
        y = self.y_speed*-1
        return y
    
    def bounce(self, state):
        TOP = 0.4
        UPPER = 0.2
        MIDDLE = 0.1
        speeds = [TOP, UPPER, MIDDLE]
        
        if self.x_speed > 0:
            multiplier = 1
        else:
            multiplier = -1
            
        #The ball moves horizontally
        if round(self.y_speed, 1) == 0:
            if state == 0:
                self.y_speed = random.randint(3, 5)
            elif state == 1:
                self.y_speed = random.randint(1, 3)
            elif state == 3:
                self.y_speed = random.randint(-3, -1)
            elif state == 4:
                self.y_speed = random.randint(-5, -3)
        
        #The ball moves downwards
        if round(self.y_speed, 1) < 0:
            if state == 0:
                self.y_speed *= (-1 - random.choice(speeds))
                self.x_speed += (TOP * multiplier)
            elif state == 1:
                self.y_speed *= (-0.5 - random.choice(speeds))
                self.x_speed += (UPPER * multiplier)
            elif state == 2:
                self.y_speed = 0
                self.x_speed -= MIDDLE
            elif state == 3:
                self.y_speed *= (0.5 + random.choice(speeds))
                self.x_speed += (UPPER * multiplier)
            elif state == 4:
                self.y_speed *= (1 + random.choice(speeds))
                self.x_speed += (TOP * multiplier)
        
        #The ball moves upwards
        elif round(self.y_speed, 1) > 0:
            if state == 0:
                self.y_speed *= (1 + random.choice(speeds))
                self.x_speed += (TOP * multiplier)
            elif state == 1:
                self.y_speed *= (0.5 + random.choice(speeds))
                self.x_speed += (UPPER * multiplier)
            elif state == 2:
                self.y_speed = 0
                self.x_speed -= MIDDLE
            elif state == 3:
                self.y_speed *= (-0.5 - random.choice(speeds))
                self.x_speed += (UPPER * multiplier)
            elif state == 4:
                self.y_speed *= (-1 - random.choice(speeds))
                self.x_speed += (TOP * multiplier)
        
        self.x_speed *= -1
        
    def move(self):
        if self.ycor() >= 225 or self.ycor() <= -345:
            self.y_speed = self.bounce_walls()
        xcord = self.xcor()
        ycord = self.ycor()
        xcord += self.x_speed
        ycord += self.y_speed
        self.goto(xcord, ycord)
        