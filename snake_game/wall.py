from turtle import Turtle, Screen


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.forward(275)
        self.left(90)
        self.pendown()
        self.forward(260)
        self.left(90)
        self.forward(560)
        self.left(90)
        self.forward(540)
        self.left(90)
        self.forward(560)
        self.left(90)
        self.forward(280)
