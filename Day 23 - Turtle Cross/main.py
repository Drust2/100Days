cls = lambda: print("\033[2J\033[;H", end='')
cls()

import turtle
import random
import time
import car
import frog
import score
"""
Day 23 - Frogger
"""
#Variables, constants and functions
screen_cars = []
car_speed = 1

#Create a car in a random interval, in a random y position
def create_car():
    ran_x = random.randint(325, 1700)
    ran_y = random.randint(-240, 240)    
    auto = car.Car(ran_x, ran_y)
    screen_cars.append(auto)

def delete_car(car):
    if car.xcor() < -325:
        car.hideturtle()
        car.clear()
        screen_cars.remove(car)
    
#Screen initialization
screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.colormode(255)
screen.title("Turtle crossing game")

#Classes initialization
player = frog.Frog()
scoreboard = score.Score()

#Functions
def exit_game():
    screen.bye()
    turtle.done()
    
#Listeners for executing the game
screen.listen()
screen.onkeypress(exit_game, "c")
screen.onkeypress(player.move, "w")

#Main loop
stop = False
while not stop:
    #Create a maximum of 20 cars on screen
    while len(screen_cars) < 15:
        create_car()
    screen.update()
    time.sleep(0.01)
    
    #Move cars and remove when necessary
    for i in screen_cars:
        i.move(car_speed)
        delete_car(i)
        
    #Clearing a level
    if player.ycor() > 300:
        car_speed += 1
        player.goto(player.x0, player.y0)
        scoreboard.update_score()
        
    #Triggering a game over
    for i in screen_cars:
        if player.ycor() - i.ycor() < 10:
            if player.distance(i) < 25:
                stop = True
                screen.update()
                scoreboard.game_over()
        else:
            if player.distance(i) < 10:
                stop = True
                screen.update()
                scoreboard.game_over()
                
turtle.done()