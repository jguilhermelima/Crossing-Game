import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tartaruga = Player()
scoreboard = Scoreboard()
carros = CarManager()

screen.listen()
screen.onkey(tartaruga.move_up, "Up")
screen.onkey(tartaruga.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carros.gerar_carros()
    carros.move_carros()

    #verificar se atravesou
    if tartaruga.chegada():
        tartaruga.reset_position()
        scoreboard.increase_level()
        carros.level_up()

    #verificar colisão
    for carro in carros.todos_carros:
        if carro.distance(tartaruga) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
