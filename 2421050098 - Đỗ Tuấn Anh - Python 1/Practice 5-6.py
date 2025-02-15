# Chương trình cho 2 số, tìm số lớn hơn

number_1 = float(input("Nhập vào số thứ nhất: "))
number_2 = float(input("Nhập vào số thứ hai: "))

if number_1 > number_2:
    print(f"{number_1} là số lớn nhất")
elif number_1 < number_2:
    print(f"{number_2} là số lớn nhất")
else:
    print(f"{number_1} = {number_2}")

# Chương trình kiểm tra một người có đủ tiêu chuẩn về chiều cao và cân nặng hay không

print("Tuyển người lao động cao trên 100cm và nặng trên 50kg")

Height = float(input("Nhập chiều cao (cm) của bạn: "))
Weight = float(input("Nhập cân nặng (kg) của bạn: "))

if Height > 100:
    if Weight > 50:
        print("Bạn đã đủ điều kiện")
    else:
        print("Bạn không đủ điều kiện")
else:
    print("Bạn không đạt chiều cao tiêu chuẩn")






























