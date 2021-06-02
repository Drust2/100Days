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

color_list = ["red", "blue", "yellow", "orange", "green", "purple"]
racers = []
screen = turtle.Screen()
screen.setup(500, 400)
x0 = -239
y0 = 125
for i in color_list:
    racer = turtle.Turtle("turtle")
    racer.color(i)
    racer.pu()
    racer.speed(0)
    racer.goto(x0, y0)
    y0 -= 50
    racers.append(racer)

user_choice = screen.textinput("Make your bet", "Who is going to win the race? Enter the color: ")

if user_choice:
    is_race_on = True
    
while is_race_on:
    for i in racers:
        distance_traveled = random.randint(0, 10)
        i.fd(distance_traveled)
        if i.xcor() > 250:
            is_race_on = False
            winner = i.pencolor()
            if user_choice.lower() == winner:
                print (f"The winner was {winner}. You win!")
                screen.bye()
                turtle.done()

            else:
                print (f"The winner was {winner}. You lose.")
                screen.bye()
                turtle.done()
            

