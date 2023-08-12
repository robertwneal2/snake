from turtle import Turtle
FONT = ('Arial', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green2')
        self.penup()
        self.shapesize(5, 5)
        self.hideturtle()
        self.goto(0, 555)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'SCORE: {self.score}    HIGH SCORE: {self.high_score}', False, 'center', FONT)
