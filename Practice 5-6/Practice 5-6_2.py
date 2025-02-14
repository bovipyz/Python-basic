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