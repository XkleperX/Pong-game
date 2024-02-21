from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 6)
        self.setheading(90)
        self.goto(x=x_axis, y=y_axis)

    def up(self):
        y = self.ycor()
        if y < 240:
            self.sety(y + 20)

    def down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - 20)
