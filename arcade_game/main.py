import time
from turtle import Turtle, Screen

from arcade_game.ball import Ball
from arcade_game.scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #     Detect if R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        r_paddle.score += 1
        print(f'R-paddle`s score: {r_paddle.score}')
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()