# Here goes everything related to the snake

# Import class "Turtle"
# Classes in python are written capitalize 
# Turtle 
from turtle import Turtle

# Build snakes body
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]

# FDefine constants for direction (it takes grades as parameters)
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
# Class constructor(activate variables, functions)
    def __init__(self):
        # Save segments of the snake
        self.segments=[] # this is an atribute of the class Snake 
        self.create_snake()
        # create atribute head
        self.head=self.segments[0]

    # Method that creates the snake 
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Add segments to snake's body
    def add_segment(self,position):
        snake_segment = Turtle("square")
        snake_segment.color("blue")
        snake_segment.penup() # Delete movement line between squares 
        snake_segment.goto(position)
        self.segments.append(snake_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):  # (start, end, step)  # It is necessary to move first the tail and then the body, ending with the head
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN: 
            self.head.setheading(UP) # Set heading is to tell direction(it is used with gradaes) 

    def down(self):
         if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
         if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    