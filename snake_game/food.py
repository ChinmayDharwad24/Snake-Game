from turtle import Turtle, Screen
from random import Random

food_pos = Random()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("yellow")
        self.refresh()

    def refresh(self):
        pos_x = food_pos.randint(-250, 250)
        pos_y = food_pos.randint(-250, 250)
        self.goto(pos_x, pos_y)



