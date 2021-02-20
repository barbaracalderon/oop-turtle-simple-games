from turtle import Turtle, Screen

jackie = Turtle()
screen = Screen()

def move_forward():
    jackie.forward(20)

def move_left():
    jackie.left(90)

def move_right():
    jackie.right(90)

def move_backward():
    jackie.backward(20)

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_backward, key="s")


screen.exitonclick()
