
import turtle
from turtle import Screen, Turtle
from Snake import Snakes
from food import Food
from Scorecard import ScoreCard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("GSMM Snake game")
screen.tracer(0)

snake = Snakes()
food = Food()
scoreboard = ScoreCard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_on = True
score = 0
while game_on:
    screen.update()
    time.sleep(0.09999)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or (snake.head.xcor() < -290) or (snake.head.ycor() > 270) or (snake.head.ycor() <-290):
        snake.snake_reset()
        scoreboard.reset()
    # if  head collides any segment of the snake body GAME OVER

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.snake_reset()
            scoreboard.reset()
screen.exitonclick()