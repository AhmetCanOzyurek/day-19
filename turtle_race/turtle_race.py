import turtle as t
import random as r
t.colormode(255)

screen = t.Screen()
screen.setup(500,400)
user_bet = screen.textinput(title= "Make your bet", prompt ="Which turtle will win the race? Enter a color: ")


tim = t.Turtle("turtle")
tom = t.Turtle("turtle")
tum = t.Turtle("turtle")
tem = t.Turtle("turtle")
tam = t.Turtle("turtle")
tomx = t.Turtle("turtle")

turtles = [tim, tom, tum, tem, tam, tomx]
positionY = -100

colors = ["red","orange","yellow","green","blue","purple"]
i=0
for turtle in turtles:
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x= -230, y = positionY)
    positionY += 30
    i += 1











screen.exitonclick()