
from turtle import Turtle
import time
from game_constants import *

class Snake:
    def __init__(self):
        """Initialize a snake on screen with a body length of three"""
        self.snake_body_array = []
        self.create_snake()
        self.head = self.snake_body_array[0]

    def create_snake(self):
        for coordinate in STARTING_COORDINATES:
            self.add_body_to_snake(coordinate)

    def add_body_to_snake(self, coordinate):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coordinate)
        self.snake_body_array.append(new_turtle)

    def extend_snake(self):
        self.add_body_to_snake( self.snake_body_array[-1].position() )

    def move(self):
        for i in range( len(self.snake_body_array)-1 , 0, -1):
            new_x = self.snake_body_array[i-1].xcor()
            new_y = self.snake_body_array[i-1].ycor()

            self.snake_body_array[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        time.sleep(SPEED)

    def get_heading(self):
        return int(self.head.heading())
    
    def set_heading(self, heading):
        self.head.setheading(heading)

    def up(self):
        if self.get_heading() != DOWN:
            self.set_heading(UP)
    
    def down(self):
        if self.get_heading() != UP:
            self.set_heading(DOWN)
    
    def left(self):
        if self.get_heading() != RIGHT:
            self.set_heading(LEFT)
    
    def right(self):
        if self.get_heading() != LEFT:
            self.set_heading(RIGHT)
