from turtle import Turtle

with open("data.txt") as data:
    high_score = data.read()

color = 'white'
alignment = 'center'
font = ('Arial', 16, 'normal')


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score

    def create_scorecard(self):
        self.penup()
        self.hideturtle()
        self.setpos(-20, 270)
        self.color(color)

    def update_scorecard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=alignment, font=font)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as new_highscore:
                new_highscore.write(str(self.high_score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.create_scorecard()
