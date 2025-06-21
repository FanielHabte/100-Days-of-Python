
class Names:
    def __init__(self, x, y):
        self.create_state_name()

    def create_state_name(self, x, y):
        self.hideturtle()
        self.penup()
        self.sety(int(y[0]))
        self.setx(int(x[0]))
        self.pendown()
        self.write(answer_state)
