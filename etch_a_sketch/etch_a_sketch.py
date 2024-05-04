import turtle as t

shem = t.Turtle()
screen = t.Screen()

def move_forwards():
    shem.forward(10)

def move_backwards():
    shem.backward(10)

def turn_left():
    shem.left(10)

def turn_right():
    shem.right(10)

def draw_circle_right():
    shem.right(10)
    shem.forward(10)
def draw_cir_left():
    shem.left(10)
    shem.forward(10)
def clear():
    shem.clear()
    shem.teleport(0,0)
    shem.seth(0)
screen.listen()
screen.onkey(key = "w",fun=move_forwards)
screen.onkey(key= "s",fun=move_backwards)


screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)



screen.exitonclick()