from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race", prompt="Choose your turtle! Enter a color name: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-60, -30, 0, 30, 60, 90]

for turtle_index in range(0, 6):
    jackie = Turtle(shape="turtle")
    jackie.color(colors[turtle_index])
    jackie.penup()
    jackie.goto(x=-220, y=y_position[turtle_index])

screen.exitonclick()