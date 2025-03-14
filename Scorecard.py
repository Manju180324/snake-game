from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score >self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()



    def increase_score(self):
        self.score += 1
        self.update_score()


