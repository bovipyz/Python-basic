# Tính điểm học phần của sinh viên và in ra màn hình
# Điểm = 0.1 * điểm C + 0.3 * điểm B + 0.6 * điểm A

a_point = float(input("Nhập điểm A: "))
b_point = float(input("Nhập điểm B: "))
c_point = float(input("Nhập điểm C: "))
if c_point <= 0:
    print("Bạn không được tính điểm")
else:
    total = 0.1 * c_point + 0.3 * b_point + 0.6 * a_point
    print(f"Tổng điểm học phần của bạn: {total}")





































