from turtle import Turtle, Screen

jackie = Turtle()
screen = Screen()

def move_forward():
    jackie.forward(10)

def move_left():
    jackie.left(10)

def move_right():
    jackie.right(10)

def move_backward():
    jackie.backward(10)

def clear_screen():
    jackie.home()
    jackie.clear()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()
