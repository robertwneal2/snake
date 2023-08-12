from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen_width = 1200
edge_detection = screen_width/2 - 10
screen_height = screen_width
screen.setup(screen_width, screen_height)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake_speed = 0.05

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if ((snake.head.xcor() > edge_detection or snake.head.xcor() < -edge_detection
            or snake.head.ycor() > edge_detection or snake.head.ycor() < -edge_detection)
            or snake.is_collision()):
        scoreboard.reset_game()
        snake.reset()
        snake.move()

screen.exitonclick()
