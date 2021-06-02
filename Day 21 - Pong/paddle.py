cls = lambda: print("\033[2J\033[;H", end='')
cls()
import turtle
"""
Day 21 - Pong - Paddle class
"""
class Paddle():
    
    def __init__(self):
        super().__init__()
        self.p1_xcord = -380
        self.p2_xcord = 375
        self.paddleparts = []
        self.create()
        self.head = self.paddleparts[0]
        self.tail = self.paddleparts[4]
        self.center = self.paddleparts[2]

    def create(self):
        y_ini = -35
        for i in range(5):
            part = turtle.Turtle()
            part.pu()
            part.speed(0)
            part.color("white")
            part.shape("square")
            part.resizemode("user")
            part.sety(y_ini)
            y_ini -= 20
            self.paddleparts.append(part)
    
    def alignment(self, player):
        if player == "p1":
            x0 = -380
        elif player == "p2":
            x0 = 380
        for i in self.paddleparts:
            i.setx(x0)
            
    
    def move_up(self):
        coord_max = self.head.ycor()
        if coord_max < 225:
            for i in self.paddleparts:
                actual = i.ycor()
                actual += 25
                i.sety(actual)
    
    def move_down(self):
        coord_min = self.tail.ycor()
        if coord_min > -345:
            for i in self.paddleparts:
                actual = i.ycor()
                actual -= 25
                i.sety(actual)


        