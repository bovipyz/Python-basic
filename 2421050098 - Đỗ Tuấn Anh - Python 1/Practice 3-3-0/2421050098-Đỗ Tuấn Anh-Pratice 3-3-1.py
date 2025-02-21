# Cho phép người dùng nhập vào 1 số
# Nếu số nhập vào không nằm trong khoảng 1 đến 10 in ra thông báo bạn đã nhập sai
# Nếu số nhập vào trong khoảng 1 đến 10 thì in ra màn hình giá trị bình phương của số nhập vào




# Cách 1: Dùng if
number = float(input("Hãy nhập vào một số: "))
if number < 1 or number > 10:
    print("Bạn đã nhập sai")
if 1 <= number <= 10:
    square = number**2
    print(f"Giá trị bình phương của số {number} là: {square}")


# Cách 2: Dùng if, else
number = float(input("Hãy nhập vào một số: "))
if 1 <= number <= 10:
    square = number**2
    print(f"Giá trị bình phương của số {number} là: {square}")
else:
    print("Bạn đã nhập sai")

    
# Cách 3: Dùng if, elif, else
number = float(input("Hãy nhập vào một số: "))
if number < 1:
    print("Bạn đã nhập sai")
elif number > 10:
    print("Bạn đã nhập sai")
else:
    square = number**2
    print(f"Giá trị bình phương của số {number} là: {square}")

































