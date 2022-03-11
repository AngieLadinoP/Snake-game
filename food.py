from turtle import Turtle
import random # gnerate random numbers

# Inherit all of turtle. 
# Pass class "Turtle" to food (between brackets)
class Food(Turtle):
    # Constructor for Food
    def __init__(self):
        # Bring everything of super class, in this case, Turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # show new food after snake's head touches it 
    def refresh(self):
        random_x=random.randint(-200,200)
        random_y=random.randint(-200,200)
        self.goto(random_x,random_y)