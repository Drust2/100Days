import turtle
import random
import time
import snake
import score
import food

cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 20/21 - Snake

Slicing: 
    letters = [a, b, c, d, e, f, g]
    printed = letters[2:5] = c, d, e
    printed = letters[2:5:2] = c, e
    printed = letters[::2] = a, c, e, g
    printed = letters[2:] = c, d, e, f, g
    printed = letters[::-1] = g, f, e, d, c, b, a
"""
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


play = True
snake = snake.Snake()   
food = food.Food()
scoreboard = score.Score()

def close():
    screen.bye()
    turtle.done()
    
screen.listen()
screen.onkey(close, "c")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


while play:
    screen.update()
    time.sleep(0.05)    
    snake.move()
    
    #Detect collision
    if snake.head.distance(food) < 15:
        food.eaten()
        scoreboard.add_point()
        snake.grow()
    
    #Detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 290 or x_cor < -290 or y_cor > 290 or y_cor < -290:
        # play = False
        scoreboard.reset()
        snake.reset()
    
    #Detect collision with head
    for i in snake.body[1:]:
        if snake.head.distance(i) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


    
