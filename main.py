from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)


screen.listen()

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")


ball = Ball()


game_is_on = True

while game_is_on:
    ball.move()
    screen.update()

    # collision for the top and bottom side
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # collision for the left and right paddle
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # right paddle
    if ball.xcor() > 380:
        ball.reset_position()

    # left paddle
    if ball.xcor() < -380:
        ball.reset_position()
screen.exitonclick()
