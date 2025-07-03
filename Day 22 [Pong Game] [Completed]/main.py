from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scores = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.refresh_time)
    screen.update()
    ball.start_game()
    scores.update_scoreboard()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >= 380:
        ball.reset_position()
        scores.l_score_update()

    if ball.xcor() <= -380:
        ball.reset_position()
        scores.r_score_update()


screen.exitonclick()
