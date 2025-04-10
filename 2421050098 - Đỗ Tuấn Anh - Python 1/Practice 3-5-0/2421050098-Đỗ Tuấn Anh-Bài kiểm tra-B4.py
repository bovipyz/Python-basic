
# Bài 1

import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.speed(100)

def draw_part():
    t.forward(100)
    t.right(35)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)


for angle in [40, 80, 120, 160, 200, 240, 280, 320, 360]:
    t.penup()
    t.home()
    t.pendown()
    t.setheading(angle)
    draw_part()

turtle.done()


# Bài 2
input_numbers = int(input("Nhập vào 1 số: "))
list_numbers = []
product_of_even_numbers = []
old_numbers = []

for i in range(input_numbers):
    input_number = int(input(f"Nhập số thứ {i + 1}: "))
    list_numbers.append(input_number)
times = 1
total_numbers_less_than_10 = 0
for number in list_numbers:
    if number % 2 == 0:
        times *= number
    elif number % 2 != 0:
        old_numbers.append(number)
        total_numbers_less_than_10 += 1
        max_old_number = max(old_numbers)
if times > 10:
    print(f"Tích các số chẵn là {times} đã lơn hơn 10")
elif total_numbers_less_than_10 == input_numbers:
    print(f"Số lẻ lớn nhất là: {max_old_number}")
elif total_numbers_less_than_10 != input_numbers:
    print(f"Tích các số chẵn nhỏ hơn 10: {times}")


# Bài 3
dic_items = {
    "táo": "VN",
    "xoài": "TQ",
    "quất": "VN",
    "cam": "VN",
    "nho": "VN",
    "xoài": "VN"
}
items_from_VN = 0
for item in dic_items:
    if dic_items[item] == "VN":
        items_from_VN += 1
print(f"Số lượng mặt hàng xuất xứ từ VN: {items_from_VN}")

















