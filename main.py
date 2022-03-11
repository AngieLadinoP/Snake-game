# Here goes what will be executed, everything related with the game functioning

# Import class "Screen " from turtel
# Classes in python are written capitalize 
# Screen 
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard  import ScoreBoard


# Board creation 
screen=Screen()  

# Create scenary
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Prográmate snake game")
screen.tracer(0) # Deactivate default aimation of turtle 

# Create snake 
snake=Snake()

#Create food
food = Food()



scoreboard=ScoreBoard()
# Event listener for keys  onkey(method, key)
screen.listen()
screen.onkey(snake.up, "Up" ) # This method doesn't have parenthesis because we need to wait for the key for it to be executed 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right") 

# movement snake
game_is_on=True
while game_is_on:
    screen.update() # control movement manually
    time.sleep(0.15) # handle time of animation (the lower the faster )
    snake.move()

# Detect collisions with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
# Detect collisions on walls
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>260 or snake.head.ycor()<-280 :
        game_is_on=False
        scoreboard.game_over()

# Detect collisions on snake's body
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()



