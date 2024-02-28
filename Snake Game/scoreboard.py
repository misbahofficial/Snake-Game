from turtle import Turtle
ALIGN = "center"
FONT_STYLE = "firacode"
FONT_SIZE = 20
FONT_WEIGHT = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.penup()
        self.write("Game Over", align=ALIGN, font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT))
        self.hideturtle()


    