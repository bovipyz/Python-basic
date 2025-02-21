import math

import turtle
window = turtle.Screen()
window.bgcolor("black")

# t = turtle
t = turtle.Turtle()
t.speed(100)
t.shape("turtle")
t.color("white")
# Vẽ hình vuông cạnh dài 150
for _ in range(4):
    t.forward(150)
    t.left(90)
# Nhấc bút
t.penup()
t.left(180)
t.forward(300)
t.pendown()
# Vẽ tam giác đều cạnh dài 200
for _ in range(3):
    t.forward(200)
    t.right(120)
# Nhấc bút
t.penup()
t.left(180)
t.forward(500)
t.right(90)
t.forward(100)
t.pendown()
t.right(90)
# vẽ hình chữ nhật cạnh dài 300, rộng 150
for _ in range(4):
    t.forward(300)
    t.right(90)
    t.forward(150)
# Nhấc bút
t.penup()
t.left(180)
t.forward(200)
t.pendown()
# Vẽ tam giác vuông cạnh dài 200
t.forward(200)
t.left(90)
t.forward(200)
t.left(135)
t.forward(200 * math.sqrt(2))

turtle.done()
