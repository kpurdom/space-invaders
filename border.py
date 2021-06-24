from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()

        # Draw border
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("white")
        self.goto(-300, -300)
        self.pendown()
        self.pensize(3)
        for side in range(4):
            self.fd(600)
            self.lt(90)
        self.penup()
