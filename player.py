from turtle import Turtle
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.left(90)
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=2)
        self.penup()
        self.goto(position)

    def move_left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, -270)

