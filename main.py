from turtle import Screen
from border import Border
from player import Player
from shoot import Shoot
from enemy import Enemy
from scoreboard import Scoreboard

FIRE_STATE = "ready"

# set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Space Invaders")
screen.tracer(0)

border = Border()
scoreboard = Scoreboard()
player = Player((0, -260))
shoot = Shoot()
enemy = Enemy()


def fire_shot():
    # function to set bullet start point equal to just above player's position (only when in 'ready' state)
    global FIRE_STATE
    if FIRE_STATE == "ready":
        FIRE_STATE = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        shoot.setposition(x, y)
        shoot.showturtle()


# define keys to control functions
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(fire_shot, "space")

# start game and make aliens move
game_is_on = True
while game_is_on:
    screen.update()
    enemy.move()

    if FIRE_STATE == "fire":
        # fire bullet straight up from player's position
        new_y = shoot.ycor() + shoot.move_speed
        shoot.sety(new_y)

        if shoot.ycor() > 275:
            # when bullet reaches the top of the screen, hide the bullet and return to 'ready' state
            shoot.hideturtle()
            FIRE_STATE = "ready"

    if not enemy.enemies:
        # When there are no aliens left on the screen, declare 'Game over - You Win'
        scoreboard.game_over("Game Over - You Win!")
        game_is_on = False
    else:
        # Otherwise, check if there have been any collisions
        for e in enemy.enemies:
            # Check for collisions between the bullet and each alien
            if shoot.distance(e["alien"]) < 10:
                e["alien"].hideturtle()
                shoot.hideturtle()
                shoot.setposition(player.xcor(), player.ycor())
                # Add points to the score board if collision occurs and return to 'ready' state
                scoreboard.update_score(e["points"])
                enemy.enemies.remove(e)
                FIRE_STATE = "ready"

            # Check for collision between the player and each alien. If collision, then game over.
            if player.distance(e["alien"]) < 10:
                scoreboard.game_over("Game Over - You Lose!")
                game_is_on = False

screen.exitonclick()
