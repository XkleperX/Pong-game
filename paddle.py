from turtle import Turtle


class Paddle:
    def __init__(self, x_axis, y_axis):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(1, 6)
        self.paddle.setheading(90)
        self.paddle.goto(x=x_axis, y=y_axis)

    def up(self):
        y = self.paddle.ycor()
        if y < 240:
            self.paddle.sety(y + 20)

    def down(self):
        y = self.paddle.ycor()
        if y > -240:
            self.paddle.sety(y - 20)
