# 3-4-1: Xây dựng chương trình in ra đoạn text sau
# # while
while True:
    numbers_input = int(input("Nhập vào một số: "))
    i = 0
    while i <= numbers_input:
        print(f"Đây là số thứ: {i}")
        i += 1  
    continuous = input("Bạn có muốn nhập tiếp không? (có/không)\n").lower()
    if continuous != "có":
        break


# for
numbers_input = int(input("Nhập vào một số: "))
for i in range(numbers_input):
  print(f"Đây là số thứ {i}")
continuous = input("Bạn có muốn nhập tiếp không? (có/không)\n").lower()
if continuous == "có":
  numbers_input = int(input("Nhập vào một số: "))
  for i in range(numbers_input):
    print(f"Đây là số thứ {i}")
elif continuous != "có":
  print("Đã dừng chương trình")
  
  
# 3-4-2: Xây dựng chương trình in ra các số từ 10 đến 100
# while
i = 10
while i <= 100:
  print(f"Đầy là số thứ {i}")
  i+=1


# for
for i in range(10, 101):
  print(f"Đây là số thứ {i}")


# 3-4-3: Xây dựng chương trình in ra các số chẵn từ 0 đến 100
# while
i = 0
while i <= 100:
  print(f"Đầy là số thứ {i}")
  i+=2


# for 
for i in range(0, 101):
  if i % 2 == 0:
    print(f"Đây là số thứ {i}")


# 3-4-4:
# Tạo một biến kiểu list để lưu tên đồ uống
# Tạo một biến kiểu list để lưu tên giá đồ uống
# In menu ra màn hình


# while 1
juices_name = ["Táo", "Cam", "Dứa"]
juices_price = [10, 20, 30]

i = 0
while i <= 2:
  print(f"{juices_name[i]} --- {juices_price[i]}")
  i += 1


# while 2
while True:
  i = 0
  juices_name = ["Táo", "Cam", "Dứa"]
  juices_price = [10, 20, 30]
  while i <= 2:
    print(f"{juices_name[i]} --- {juices_price[i]}")
    i += 1
  break
# for 
juices_name = ["Táo", "Cam", "Dứa"]
juices_price = [10, 20, 30]

for i in range(0, 3):
  print(f"{juices_name[i]} --- {juices_price[i]}")


# 3-4-5: 
# In danh sách đồ uống ra màn hình
# In danh sách đồ uống và giá tiền của nó ra màn hình

# while 1
juices_price = ["Táo", "Cam", "Dứa", 10, 20, 30]
i = 0
print("Danh sách đồ uống:")
while i <= 2:
  print(f"{juices_price[i]}")
  i += 1
i = 0
while i <= 2:
  print(f"{juices_price[i]} --- {juices_price[i + 3]}")
  i += 1


# while 2
while True:
  i = 0
  juices_price = ["Táo", "Cam", "Dứa", 10, 20, 30]
  print("Danh sách đồ uống:")
  while i <= 2:
    print(f"{juices_price[i]}", end = "\n")
    i += 1
    continue
  i = 0
  while i <=2:
    print(f"{juices_price[i]} --- {juices_price[i + 3]}")
    i+=1
  break


# for
juices_price = ["Táo", "Cam", "Dứa", 10, 20, 30]
for i in range(0, 3):
  print(f"{juices_price[i]} --- {juices_price[i + 3]}")
print("Danh sách đồ uống")
for i in range(0, 3):
  print(f"{juices_price[i]}", end = " ")


# 3-4-6: 
# In danh sách đồ uống ra màn hình sử dụng for
# In danh sách đồ uống và giá tiền của nó ra màn hình sử dụng for

# for
juices_price = ["Táo", "Cam", "Dứa", 10, 20, 30]
for i in range(0, 3):
  print(f"{juices_price[i]} --- {juices_price[i + 3]}")
print("Danh sách đồ uống")
for i in range(0, 3):
  print(f"{juices_price[i]}", end = " ")


# 3-4-7: 
# In danh sách đồ uống ra màn hình sử dụng for in
# In danh sách đồ uống và giá tiền của nó ra màn hình sử dụng for in

# for
juices_price = ["Táo", "Cam", "Dứa", 10, 20, 30]
for i in range(0, 3):
  print(f"{juices_price[i]} --- {juices_price[i + 3]}")
print("Danh sách đồ uống")
for i in range(0, 3):
  print(f"{juices_price[i]}", end = " ")






































