from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(1, 6)
paddle.setheading(90)
paddle.goto(350, 0)


def up():
    y = paddle.ycor()
    if y < 240:
        paddle.sety(y + 20)


def down():
    y = paddle.ycor()
    if y > -240:
        paddle.sety(y - 20)


screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")

screen.update()
screen.exitonclick()
