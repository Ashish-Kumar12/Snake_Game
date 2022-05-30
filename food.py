
from turtle import Turtle 
import random
from game_constants import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-BOUNDARY, BOUNDARY)
        random_y = random.randint(-BOUNDARY, BOUNDARY)
        self.goto(random_x, random_y)
