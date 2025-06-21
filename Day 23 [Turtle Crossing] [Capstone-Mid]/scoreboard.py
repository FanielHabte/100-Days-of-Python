from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1

    def update_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.write(f"Level:{self.score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)

