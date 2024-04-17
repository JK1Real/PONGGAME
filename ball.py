#Create ball and make it move

from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.x_move = 5
        self.y_move = 5


    def createball(self):
        self.shape(name="circle")
        self.shapesize(1)
        self.color("red")
        self.penup()
        self.goto(x=0,y=0)

    def move(self):
        new_x = self.xcor() +self.x_move
        new_y =self.ycor() +self.y_move

        self.goto(new_x, new_y)

 


    def bounce(self):
        self.y_move*=-1

    def padle_bounce(self):
        self.x_move*=-1

    def refresh(self):
        self.goto(x=0,y=0)
        self.padle_bounce()
    
    

        