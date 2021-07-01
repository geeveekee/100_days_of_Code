from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("100_days_of_Code\d24\data.txt") as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("white")
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("100_days_of_Code\d24\data.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    """ def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal")) """

        


        
    
