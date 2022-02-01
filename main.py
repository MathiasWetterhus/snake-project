from turtle import Screen
import time
from snake import Snake
import food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("royal blue")
screen.title("Mathias Snake Game")
screen.tracer(0)


snake = Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

snake.construct_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    scoreboard.display_score()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add_to_score()
        snake.extend()
        print('nom nom nom')

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False

    #Detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over

scoreboard.game_over()

screen.exitonclick()