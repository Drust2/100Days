import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = round(random.random()*100, 2)
randomnumS = str(randomnum)

"""
Day 6 - Functions & Karel

Making functions: 
def - Keyword to define a function
    def my_function():
        print("Hello")
        print("Bye")
        
So, after calling the function, we'll get it to execute:
    my_function()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

counter = 0
for n in range(6):
    jump()

while - Performs a loop while a condition stays true
"""
