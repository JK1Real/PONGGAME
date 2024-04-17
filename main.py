# Create the screen

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

from time import sleep

sleep_time = 0.05
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle()
r_paddle.create_paddle([350,0])


l_paddle = Paddle()
l_paddle.create_paddle([-350,0])


screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

#Create another paddle
screen.onkey(l_paddle.move_up,"q")
screen.onkey(l_paddle.move_down,"z")


ball = Ball()
ball.createball()


scoreboard = Scoreboard()


scoreboard1 = Scoreboard()


game_is_on = True

while game_is_on:

    sleep(sleep_time)
    screen.update()
    ball.move()

    scoreboard.board((-300,250))
    scoreboard1.board((200,250))


    # Detect the collision with wall and make it move
    if ball.ycor() >200 or ball.ycor() <-200:
        # Detect collision with wall and bounce 
        ball.bounce()
        
    # When ball collides the paddle
    if (r_paddle.distance(ball.pos()) <34 and ball.xcor() > 329) or  (l_paddle.distance(ball.pos()) <34 and ball.xcor() <-329):
        ball.padle_bounce()
        sleep_time*=.09

    # When the ball misses the paddle
    if ball.xcor() > 330:
        scoreboard.scoreup()
        ball.refresh()
        sleep_time = 0.05
    
    if ball.xcor() < -330:
        scoreboard1.scoreup()
        ball.refresh()
        sleep_time = 0.05





screen.exitonclick()