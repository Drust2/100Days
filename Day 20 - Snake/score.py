from turtle import Turtle
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 20/21 - Score class
"""
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.score=0
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.pd()
        self.write(f"Score: {self.score}   |   Highscore: {self.highscore}", False, "center", font=("Tahoma", 12, "bold"))
    
    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}   |   Highscore: {self.highscore}", False, "center", font=("Tahoma", 12, "bold"))

    def game_over(self):
        self.pu()
        self.home()
        self.clear()
        self.write("Game Over", False, "center", font=("Courier", 24, "bold"))
    
    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            with open("data.txt", "r") as file:
                self.highscore = int(file.read())
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}   |   Highscore: {self.highscore}", False, "center", font=("Tahoma", 12, "bold"))
            
        