import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scorecard = Level()

screen.listen()
screen.onkey(key="Up", fun=player.move)

number_of_refresh = 0
sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    player.create_turtle()
    scorecard.update_scoreboard()
    car_manager.move_cars()

    # Create a car every 6 refreshes
    if number_of_refresh == 0 or number_of_refresh == 6:
        car_manager.create_car()
        number_of_refresh = 0

    # Detect player crossed the other side
    if player.ycor() > 280:
        scorecard.increase_score()  # increases the score by 1
        player.return_home()  # return the player to starting point
        car_manager.level_up()  # increases the speed of the cars

    # Detect collision with the cars
    for car in car_manager.car_list:
        if car.distance(player.pos()) < 20:
            game_is_on = False
            scorecard.game_over()  # print game-over on screen

    number_of_refresh += 1

screen.exitonclick()
