from turtle import Turtle


class Shoot(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.setheading(90)
        self.speed(0)
        self.move_speed = 0.25
        self.penup()
        self.hideturtle()


