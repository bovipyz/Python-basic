import math

import turtle
window = turtle.Screen()
window.bgcolor("black")

# t = turtle
t = turtle.Turtle()
t.speed(100)
t.shape("turtle")
t.color("white")

# Vẽ hình thoi có cạnh dài 150
t.right(30)
t.forward(150)
t.left(60)
t.forward(150)
t.left(120)
t.forward(150)
t.left(60)
t.forward(150)
t.right(30)

# Nhâc bút
t.penup()
t.forward(200)
t.pendown()

# Vẽ hình thang có cạnh ngắn dài 200 và cạnh dài dài 400
t.forward(200)
t.left(45)
t.forward(141)
t.left(135)
t.forward(400)
t.left(135)
t.forward(141)
t.left(45)
t.forward(200) 

t.hideturtle()
turtle.done()














