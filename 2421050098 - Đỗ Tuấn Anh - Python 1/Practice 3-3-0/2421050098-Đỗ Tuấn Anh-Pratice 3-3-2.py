# Viết chương trình cho phép người dùng nhâp hình mình muốn vẽ (ví dụ: tam giác, vuông, tròn, …)
# Chương trình vẽ hình theo đúng yêu cầu nhập vào của người dùng

import turtle


# Cách 1: Dùng if
list = ["tam giác", "vuông", "tròn"]
t = input("Hãy nhập vào 1 trong 3 hình (tam giác, vuông, tròn) muốn vẽ: ").lower()
if t in list:
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(100)
    if t == "tam giác":
        for i in range(3):
            pen.forward(100)
            pen.right(120)
        print("Đã vẽ hình tam giác")
    if t == "vuông":
        for i in range(4):
            pen.forward(100)
            pen.right(90)
        print("Đã vẽ hình vuông")
    if t == "tròn":
        for i in range(4):
            pen.circle(50)
        print("Đã vẽ hình tròn")
    turtle.done()
if t not in list:
    print("Hình không phù hợp")



# Cách 2: Dùng if, else
list = ["tam giác", "vuông", "tròn"]
t = input("Hãy nhập vào 1 trong 3 hình (tam giác, vuông, tròn) muốn vẽ: ").lower()
if t in list:
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(100)
    if t == "tam giác":
        for i in range(3):
            pen.forward(100)
            pen.right(120)
        print("Đã vẽ hình tam giác")
    if t == "vuông":
        for i in range(4):
            pen.forward(100)
            pen.right(90)
        print("Đã vẽ hình vuông")
    if t == "tròn":
        for i in range(4):
            pen.circle(50)
        print("Đã vẽ hình tròn")
    turtle.done()
else:
    print("Hình không phù hợp")



# Cách 3: Dùng if, elif, else
list = ["tam giác", "vuông", "tròn"]
t = input("Hãy nhập vào 1 trong 3 hình (tam giác, vuông, tròn) muốn vẽ: ").lower()
if t in list:
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(100)
    if t == "tam giác":
        for i in range(3):
            pen.forward(100)
            pen.right(120)
        print("Đã vẽ hình tam giác")
    elif t == "vuông":
        for i in range(4):
            pen.forward(100)
            pen.right(90)
        print("Đã vẽ hình vuông")
    elif t == "tròn":
        for i in range(4):
            pen.circle(50)
        print("Đã vẽ hình tròn")
    turtle.done()
else:
    print("Hình không phù hợp")
































































