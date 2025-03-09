# Bài toán
# 1. Lưu menu của quán trà chanh vào 1 list, in danh sách ra màn hình, cho phép người dùng thêm món mới vào trong menu

# for
juices_name = ["Đào", 10, "Cam", 20, "Tắc", 30, "chanh", 40]
print(f"Danh sách đồ uống hiện tại: {juices_name}")

numbers_input = int(input("Nhập số lượng nước trà bạn muốn thêm: "))
for i in range(numbers_input):
  new_juice = input(f"Nhập tên nước trà thứ {i + 1}: ")
  new_price = int(input(f"Nhập giá cảu trà thứ {i + 1}: "))
  juices_name.append(new_juice)
  juices_name.append(new_price)
print(f"Danh sách sau khi thêm: {juices_name}")
more_input = input("Bạn có muốn nhập tiếp không? (Có/Không)\n").lower()
if more_input != "có":
  print("")
else:
  numbers_input = int(input("Nhập số lượng nước trà bạn muốn thêm: "))
  for i in range(numbers_input):
    new_juice = input(f"Nhập tên nước trà thứ {i + 1}: ")
    new_price = int(input(f"Nhập giá của trà thứ {i + 1}: "))
    juices_name.append(new_juice)
    juices_name.append(new_price)
  print(f"Danh sách sau khi thêm: {juices_name}")


# while 1
juices_name = ["Đào", 10, "Cam", 20, "Tắc", 30]
print(f"Danh sách đồ uống hiện tại: {juices_name}")

while True:
  i = 0
  numbers_input = int(input("Nhập số lượng nước trà bạn muốn thêm: "))
  while i < numbers_input:
    new_juice = input(f"Nhập tên nước trà thứ {i + 1}: ")
    new_price = int(input(f"Nhập giá cảu trà thứ {i + 1}: "))
    juices_name.append(new_juice)
    juices_name.append(new_price)
    i += 1
  print(f"Danh sách sau khi thêm: {juices_name}")
  more_input = input("Bạn có muốn nhập thêm nữa không? (Có/Không)\n").lower()
  if more_input != "có":
    break


# while 2
juices_name = ["Đào", 10, "Cam", 20, "Tắc", 30]
print(f"Danh sách đồ uống hiện tại: {juices_name}")

continue_input = "có"
while continue_input == "có":
    numbers_input = int(input("Nhập số lượng nước trà bạn muốn thêm: "))
    i = 0
    while i < numbers_input:
        new_juice = input(f"Nhập tên nước trà thứ {i + 1}: ")
        new_price = int(input(f"Nhập giá của trà thứ {i + 1}: "))
        juices_name.append(new_juice)
        juices_name.append(new_price)
        i += 1
    print(f"Danh sách sau khi thêm: {juices_name}")
    continue_input = input("Bạn có muốn nhập tiếp không? (Có/Không)\n").lower()



# 2. 
# - Lưu 5 món ăn và giá tiền vào 1 biến
# - Cho phép người dùng gõ tên 1 món ăn và số lượng muốn mua
# - Tính tiền nếu món ăn có trong menu
# - In ra thông báo “không có món ăn bạn vừa chọn” nếu món ăn không có trong menu

# for
foods_price = [["tôm", "cua", "cá", "ốc", "mực"], [10, 20, 30, 40, 50]]
food_name = input("Nhập tên món ăn muốn mua: ").lower()

for i in range(len(foods_price[0])):
    if food_name == foods_price[0][i]:
        input_quantity = int(input("Nhập số lượng: "))
        total = foods_price[1][i] * input_quantity
        print(f"Tổng số tiền phải trả: {total}")
        break  
else:
    print("Món ăn không có trong danh sách.")


# while 1
foods_price = ["tôm", 10, "cua", 20, "cá", 30, "ốc", 40, "mực", 50]
continue_program = True

while continue_program:
    food_name = input("Nhập tên món ăn muốn mua: ").lower()
    if food_name in [foods_price[i].lower() for i in range(0, len(foods_price), 2)]:
        i = [foods_price[i].lower() for i in range(0, len(foods_price), 2)].index(food_name) * 2
        input_quantity = int(input("Nhập số lượng: "))
        total = foods_price[i + 1] * input_quantity
        print(f"Tổng số tiền phải trả: {total}")
    else:
        print("Món ăn không có trong danh sách.")
    continue_program = input("Bạn có muốn thử lại không? (Có/Không):\n").lower()
    if continue_program != "có":
        # continue_program = False
        break
print("Kết thúc chương trình")


# while 2
foods_price = [["tôm", 10], ["cua", 20], ["cá", 30], ["ốc", 40], ["mực", 50]]

while True:
    food_name = input("Nhập tên món ăn muốn mua: ").lower()
    for i in foods_price:
        if i[0].lower() == food_name:
            input_quantity = int(input("Nhập số lượng: "))
            total = i[1] * input_quantity
            print(f"Tổng số tiền phải trả: {total}")
            break
    continue_program = input("Bạn có muốn mua tiếp không? (Có/không):\n").lower()
    if continue_program != "có":
        break
print("Kết thúc chương trình")        



# 3. Lưu menu và giá tiền của quán trà chanh vào 1 list, in menu và giá tiền ra màn hình
# for
juices_name = ["Đào", 10, "Cam", 20, "Tắc", 30, "chanh", 40]
print(f"Danh sách đồ uống quán trà tranh: ")
for i in range(0, len(juices_name), 2):
    print(f"{juices_name[i]} -- {juices_name[i + 1]}")


# while 1
juices_name = ["Đào", 10, "Cam", 20, "Tắc", 30, "chanh", 40]
print(f"Danh sách đồ uống quán trà tranh: ")
i = 0
while i < len(juices_name):
  print(f"{juices_name[i]} -- {juices_name[i + 1]}")
  i += 2


# while 2
juices_name = [["Đào", 10], ["Cam", 20], ["Tắc", 30], ["chanh", 40]]
print(f"Danh sách đồ uống quán trà tranh: ")

while True:
    for i in juices_name:
        print(f"{i[0]} -- {i[1]}")
    break



# 4. Cho phép người dùng nhập vào n số, tính tổng các số người dùng đã nhập vào
# for
number_input = int(input("Nhập vào một số: "))
total = 0

for i in range(1, number_input + 1):
    total += i
print(f"Tổng: {total}")
  

# while 1
number_input = int(input("Nhập vào một số: "))
i = 0
total = 0

while i < number_input:
    i += 1
    total += i
print(f"Tổng: {total}")


# while 2

while True:
    # total = 0
    # number_input = int(input("Nhập vào một số: "))
    # for i in range(1, number_input + 1):
    #     total += i
    # print(f"Tổng: {total}")
    # break
    number_input = int(input("Nhập vào một số: "))
    i = 0
    total = 0
    while i < number_input:
        i += 1
        total += i
    print(f"Tổng: {total}")
    break











  

















































