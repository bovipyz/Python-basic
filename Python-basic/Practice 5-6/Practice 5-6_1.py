# Chương trình cho 2 số, tìm số lớn hơn

number_1 = float(input("Nhập vào số thứ nhất: "))
number_2 = float(input("Nhập vào số thứ hai: "))

if number_1 > number_2:
    print(f"{number_1} là số lớn nhất")
elif number_1 < number_2:
    print(f"{number_2} là số lớn nhất")
else:
    print(f"{number_1} = {number_2}")