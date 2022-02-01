from turtle import Turtle
ALIGNEMENT = "center"
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        self.current_score = 0
        super().__init__()
        self.color("white")




    def display_score(self):
        self.penup()
        self.hideturtle()
        self.clear()
        self.sety(270)
        self.write(arg=f"Score: {self.current_score}", align=ALIGNEMENT, font=FONT)


    def add_to_score(self):
        self.current_score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align=ALIGNEMENT, font=FONT)