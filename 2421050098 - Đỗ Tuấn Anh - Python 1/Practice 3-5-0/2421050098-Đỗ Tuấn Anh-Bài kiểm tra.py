# Bài 1
import turtle
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(100)
def draw_part(t):
    pen.forward(80)
    pen.right(35)
    pen.circle(10)
    pen.forward(30)
    pen.circle(10)

for i in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]:
    pen.penup()
    pen.home()
    pen.pendown()
    pen.setheading(i)
    draw_part(pen)

turtle.done()

# Bài 2

input_numbers = int(input("Nhập vào n số: "))
list_number = []
new_list_number = []
total = 0
for i in range(input_numbers):
    input_number = float(input(f"Nhập số thứ {i + 1}: "))
    list_number.append(input_number)
for number in list_number:
    if number > 10:
        new_list_number.append(number)
        total += i

if total == 0:
    print("Không có số nào lớn hơn 10")
else:
    print(f"Danh sách các số lớn hơn 10: {new_list_number}")


# Bài 3
phone_name_price = {
    "Samsung": 1000000,
    "oppo": 2000000,
    "xiaomi": 3000000,
    "bphone": 4000000,
    "iphone": 5000000,
    "nokia": 6000000,
    "huawei": 7000000,
    "samsung xs": 80000000
}
print("------Tên và giá của các loại điện thoại-----")
for name, price in phone_name_price.items():
    print(f"Tên điện thoại: {name} --- giá: {price} đồng")
average_price = 5000000
new_list_phone = {}
total = 0
for name in phone_name_price:
    if phone_name_price[name] > average_price:
        new_list_phone[name] = phone_name_price[name]
        total += 1
print(f"Danh sách các loại điện thoại có giá trên 5 triệu đồng: {new_list_phone}")
print(f"Số lượng điện thoại có giá trên 5 triệu đồng: {total}")




























