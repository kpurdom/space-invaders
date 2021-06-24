from turtle import Turtle, register_shape
MOVE_DISTANCE = 0.1
NUM_ENEMIES = 8
NUM_ROWS = 3


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-310, -310)
        register_shape("invaders.gif")
        self.enemies = []
        self.create_enemies()
        self.direction = 1

    def create_enemies(self):
        for row in range(NUM_ROWS):
            for num in range(NUM_ENEMIES):
                new_enemy = Turtle("invaders.gif")
                new_enemy.penup()
                new_enemy.goto(-270 + num * 50, 160 + row * 50)
                enemy_info = {"alien": new_enemy, "points": (row + 1) * 10}
                self.enemies.append(enemy_info)

    def move(self):
        for enemy in self.enemies:
            alien = enemy["alien"]
            x = alien.xcor() + MOVE_DISTANCE * self.direction
            alien.setx(x)
            if alien.xcor() < -270 or alien.xcor() > 270:
                self.direction *= -1
                for e in self.enemies:
                    y = e["alien"].ycor() - 30
                    e["alien"].sety(y)