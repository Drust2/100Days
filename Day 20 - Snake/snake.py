import turtle
import time
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 20/21 - Snake class
"""

class Snake:
    
    #Initialize the Snake body
    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]
    
    def create(self):
        x0_pos = 0
        for i in range(3):
            snek = turtle.Turtle()
            snek.shape("square")
            snek.color("white", "red")
            snek.pu()
            snek.speed(0)
            snek.setx(x0_pos)
            self.body.append(snek)
            x0_pos -= 20
    
    def new_tail(self, position):
        snek = turtle.Turtle()
        snek.shape("square")
        snek.color("white", "red")
        snek.pu()
        snek.speed(0)
        snek.goto(position)        
        self.body.append(snek)
        return snek        
        
    def grow(self):
        position = len(self.body)-1
        new_tail = self.body[position].position()
        self.new_tail(new_tail)
    
    def move(self):
        #Following the head
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x, new_y)
        #Moving forward
        self.head.fd(20)
            
    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)
    
    def down(self):
        if self.head.heading() == 180:
            self.head.left(90)
        elif self.head.heading() == 0:
            self.head.right(90)
            
    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)
            
    def right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        elif self.head.heading() == 90:
            self.head.right(90)
    
    def reset(self):
        for i in self.body:
            i.hideturtle()
            i.clear()
        self.body.clear()
        self.create()
        self.head = self.body[0]
        time.sleep(1)