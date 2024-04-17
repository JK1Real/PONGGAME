from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.score = 0
    
    def board(self,position):

        self.hideturtle()
        self.goto(position)
        self.color("blue")
        self.write(f" Score : {self.score}", font=("Arial", 24, "normal"))

    def scoreup(self):
        self.clear()
        self.score+=1
        
        
        