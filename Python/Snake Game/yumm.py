import time
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")




class Yumm(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()

    def yummy(self):
        self.goto(0, 0)
        self.write("YUMMY!", align="center", font=FONT)
        # time.sleep(0.1)
        self.clear()

