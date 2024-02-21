from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_axis = 0.1
        self.y_axis = 0.1
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_axis
        y = self.ycor() + self.y_axis
        self.goto(x, y)

    def bounce_y(self):
        self.y_axis *= -1

    def bounce_x(self):
        self.x_axis *= -1
        self.move_speed *= 0.9

    def reset_position(self):
      self.goto(0, 0)
      self.bounce_x()
      self.y_axis = 0.1  # Reset y-axis direction

