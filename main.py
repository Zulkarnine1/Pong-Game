# Imports
from turtle import Turtle, Screen
from player_board import PlayerBoard, EnemyBoard
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(0,-1*screen.screensize()[1])
line.pendown()
line.setheading(90)
line.speed(0)
line.pensize(6)
for i in range(-1*screen.screensize()[1],1*screen.screensize()[0],15):
    if i%2==0:
        line.pendown()
        line.forward(15)
    else:
        line.penup()
        line.forward(15)

score = ScoreBoard()
p_board = PlayerBoard(350,0)
e_board = PlayerBoard(-350,0)
ball = Ball()

screen.listen()
screen.onkey(p_board.move_up, "Up")
screen.onkey(p_board.move_down, "Down")
screen.onkey(e_board.move_up, "w")
screen.onkey(e_board.move_down, "s")

game_on = True
sleep_time = 0.008
while game_on:
    screen.update()
    ball.move()
    time.sleep(sleep_time)

    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(p_board) < 50 and ball.xcor()>320 or ball.distance(e_board) < 50 and ball.xcor()<-320 :
        ball.bounce_x()
        sleep_time *= 0.9

    if ball.xcor()>340 :
        ball.relocate()
        score.l_score += 1
        score.print_score()
        sleep_time = 0.008

    if ball.xcor()<-340:
        ball.relocate()
        score.r_score += 1
        score.print_score()
        sleep_time = 0.008




screen.exitonclick()

# Create Screen