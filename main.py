from turtle import Turtle,Screen
import time
from snake import snake
from food import Food
from scoreboard import scoreBoard



food = Food()

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# segments = []

snake = snake()
score = scoreBoard()

screen.listen()
screen.onkeypress(snake.move_up,"Up")
screen.onkeypress(snake.move_down,"Down")
screen.onkeypress(snake.move_left,"Left")
screen.onkeypress(snake.move_right,"Right")

is_race_on = True

while is_race_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detecting contact 
        if snake.head.distance(food) < 15 :
                food.refresh()
                snake.extend()
                score.increase_score()


        if snake.head.xcor() >= 291 or snake.head.xcor() <= -291 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295  :
                is_race_on = False     
                score.game_over()  


        for segment in snake.segments[1:]:    
                if snake.head.distance(segment) < 10:
                        is_race_on = False
                        score.game_over() 


screen.exitonclick()