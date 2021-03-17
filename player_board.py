from turtle import Turtle

class PlayerBoard(Turtle):


    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.speed(3)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)



    def move_up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-30)



class EnemyBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(-350,0)
        self.speed(3)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
