from turtle import Turtle


# Constants for score
FONT =("Poppins",20,"bold")
ALIGN="center"

# Inherit everything from "Turtle"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")

        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"El puntaje es: {self.score} ", font=FONT, align=ALIGN)
    
    def increase_score(self):
        self.clear() # Erase the previous number otherwise it will be written over the previous one
        self.score+=1
        self.update_score()

    def game_over(self):
        self.clear() # Erase the previous number
        self.write("Juego terminado", font=FONT, align=ALIGN)