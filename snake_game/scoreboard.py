from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.color("white")
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=FONT, align=ALIGN)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", font=FONT, align=ALIGN)


