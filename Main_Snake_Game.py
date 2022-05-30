
from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_constants import *

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width= SCREEN_SIZE, height= SCREEN_SIZE)
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def collision_with_food():
    food.refresh()
    snake.extend_snake()
    scoreboard.increase_score()

def collision_with_wall():
    scoreboard.game_over()

def collision_with_body():
    scoreboard.game_over()

while game_is_on:
    snake.move()
    screen.update()

    # Detect collision with food
    if snake.head.distance( food ) < COLLISION:
        collision_with_food()

    # Detect collision with wall
    if snake.head.xcor() < -BOUNDARY or snake.head.xcor() > BOUNDARY or snake.head.ycor() < -BOUNDARY or snake.head.ycor() > BOUNDARY:
        collision_with_wall()
        game_is_on = False

    # Detect collision with body
    for segment in snake.snake_body_array[1:]:
        if snake.head.distance(segment) < COLLISION:
            collision_with_body()
            game_is_on = False 

screen.exitonclick()
