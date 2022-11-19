from turtle import Turtle
# import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.initial()
        self.head = self.segment[0]

    def initial(self):
        for pos in STARTING_POSITIONS:  # Snake setup
            self.add_segment(pos)

    def add_segment(self, position):
        add_block = Turtle()
        add_block.shape("square")
        add_block.color("white")
        add_block.penup()
        add_block.goto(position)
        self.segment.append(add_block)

    def movement(self):
        # for snake in self.segment:
        #     snake.penup()
        #     snake.speed("slowest")

        for i in range(len(self.segment) - 1, 0, -1):
            next_pos = self.segment[i - 1].position()
            self.segment[i].goto(next_pos)
        self.segment[0].forward(20)

    def extend(self):
        self.add_segment(self.segment[-1].position())
        # time.sleep(1)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.initial()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        # print(self.head.heading())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        # self.segment[0].left(90)
        # self.segment[0].forward(20)

