from turtle import Turtle


#Create and move the paddle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self,pos):
        self.speed(0)
        self.pos = pos
        self.color("white")
        self.shape(name="square")
        self.shapesize(stretch_len=1,stretch_wid=3)
        self.penup()
        self.goto(self.pos[0],self.pos[1])

    def move_up(self):
        self.new_y = self.ycor() +20
        self.goto(self.xcor(),self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(),self.new_y)