from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_bet = screen.textinput(title="Turtle Race", prompt="Choose your turtle! Enter a color name: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-60, -30, 0, 30, 60, 90]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} is the winning turtle!')
            else:
                print(f'You lost. The {winning_color} is the winning turtle!')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
