import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move,'Up')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    # Detect a successful crossing
    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset()
        cars.level_up()

#         Detect the collision with the car
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False




screen.onscreenclick()

