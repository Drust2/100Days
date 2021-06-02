cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 19 - Instances, State and Higher Order Functions
#Etch-A-Sketch and Turtle Race

The function is not called with the parenthesis as:
def functionA(n1, n2):
  print(f"Hello {n1} + {n2}")

def functionB(n1, n2, func):
  func(n1,n2)
Function is called inside when entered as a parameter. So:
functionB(a, b, functionA)

This is a Higher order function.
"""
import turtle 
import random

turt = turtle.Turtle()
turt.speed(0)
screen = turtle.Screen()

def move_forwards():
    turt.fd(10)
def move_backwards():
    turt.bk(10)
def turn_left():
    turt.lt(10)
def turn_right():
    turt.rt(10)
def clear():
    turt.clear()
    turt.pu()
    turt.home()
    turt.pd()
    
screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
turtle.done()
turtle.bye()