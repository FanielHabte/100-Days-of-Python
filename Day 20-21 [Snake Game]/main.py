import time
from turtle import Screen
from snake import Snake
from food import Food
from scorecard import ScoreCard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreCard()
scoreboard.create_scorecard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


not_failed = True
while not_failed:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.update_scorecard()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            scoreboard.reset()


screen.exitonclick()
