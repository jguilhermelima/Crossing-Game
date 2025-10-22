from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.todos_carros=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def gerar_carros(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_carro = Turtle()
            new_carro.shape("square")
            new_carro.penup()
            new_carro.goto(280, random.randint(-250, 280))
            new_carro.color(random.choice(COLORS))
            new_carro.setheading(180)
            new_carro.shapesize(stretch_len=2,stretch_wid=1)
            self.todos_carros.append(new_carro)

    def move_carros(self):
        for carro in self.todos_carros:
            carro.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

