cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 21 - Pong
"""
import turtle
import time
import paddle
import ball
import stats
import score
import random

screen = turtle.Screen()
screen.setup(800, 750)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

#Close the game with a defined key
def close():
    screen.bye()
    turtle.done()

    
paddle1 = paddle.Paddle() 
paddle1.alignment("p1")

paddle2 = paddle.Paddle() 
paddle2.alignment("p2")

ball = ball.Ball()
#stats = stats.Stats()
scoreboard = score.Score()

#Check if a paddle hits the ball to execute the bounce of the ball.
def hit(paddle):
    counter = 0
    for i in paddle.paddleparts:
        if i.distance(ball) < 17:
            return counter
        else:
            counter += 1
    return -1

#Controls
screen.listen()
screen.onkeypress(close, "c")
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")

play = True
while play:
    # stats.xcoord = ball.xcor()
    # stats.ycoord = ball.ycor()
    # stats.tracking()
    screen.update()    
    ball.move()
    time.sleep(0.01)
    
    #Check if the ball hits a segment of the paddle
    paddle1_part_hit = hit(paddle1)
    if paddle1_part_hit > -1:
        ball.bounce(paddle1_part_hit)
    paddle2_part_hit = hit(paddle2)
    if paddle2_part_hit > -1:
        ball.bounce(paddle2_part_hit)
    
    #Adds to the score, resets the ball and the initial speed and adds a 3 second delay
    if ball.xcor() < -380:
        scoreboard.score(2)
        ball.home()
        ball.x_speed = 3
        ball.y_speed = 5*random.choice([-1, 1])
        screen.update() 
        time.sleep(3)
    elif ball.xcor() > 380:
        scoreboard.score(1)
        ball.home()
        ball.x_speed = -3
        ball.y_speed = 5*random.choice([-1, 1])
        screen.update() 
        time.sleep(3)


