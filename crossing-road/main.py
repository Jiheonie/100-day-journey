from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


player = Player()
player.control()


scoreboard = Scoreboard()


car_manager = CarManager()
car_list = car_manager.car_list


turn = 0
car_create_interval = 10

is_on = True
while is_on:
    sleep(0.01)
    screen.update()
    if turn % car_create_interval == 0:
        car_manager.add_car()
    turn += 1
    car_manager.move()
    
    if player.reach_finish():
        scoreboard.level += 1
        player.start()
        car_manager.speed_up()
    
    if player.crash(car_list):
        scoreboard.game_over()
        print(f"You reached {scoreboard.level}")
        break

    scoreboard.update()


screen.exitonclick()