from turtle import Screen
from food import Food
from wall import Wall
from snake import Snake
from scoreboard import ScoreBoard
import time


screen = Screen()
game = True
screen.setup(width=600, height=600)          # Screen setup
screen.bgcolor("black")
screen.title("My Childhood Game")
screen.tracer(0)

cobra = Snake()
food = Food()
wall = Wall()
score_count = ScoreBoard()
screen.listen()


while game is True:
    cobra.movement()
    screen.onkey(cobra.up, "Up")
    screen.onkey(cobra.down, "Down")
    screen.onkey(cobra.left, "Left")
    screen.onkey(cobra.right, "Right")
    screen.update()                          # Screen is getting updated every 1 sec
    time.sleep(0.2)
    # hit_x = food.xcor()
    # hit_y = food.ycor()

    # Detect collision with food
    if cobra.head.distance(food) < 15:
        food.refresh()
        cobra.extend()
        score_count.increase_score()

    # Detect collision with wall
    if cobra.head.xcor() > 257 or cobra.head.xcor() < -260 \
            or cobra.head.ycor() > 240 or cobra.head.ycor() < -259.9:
        # game = False
        score_count.reset()
        time.sleep(0.5)
        cobra.reset()

    # Detect collision with tail
    for segment in cobra.segment[1:len(cobra.segment)]:
        # if segment == cobra.head:
        #     continue
        if cobra.head.distance(segment) < 10:
            # game = False
            score_count.reset()
            time.sleep(0.5)
            cobra.reset()


score_count.game_over()
screen.exitonclick()


# sammy1.shape("square")
# sammy1.color("white")
# sammy2.shape("square")
# sammy2.color("white")
# sammy2.goto(20, 0)
# sammy3.shape("square")
# sammy3.color("white")
# sammy3.goto(-20, 0)








