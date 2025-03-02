# Sinh viên sử dụng vòng lặp while để xây dựng lại các bài toán đã làm với for


# 3-4-1, 3-4-2
input_number = int(input("Nhập số bắt đầu: "))
output_number = int(input("Nhập số kết thúc: "))
while input_number <= output_number:
    print(f"Đây là số thứ {input_number}")
    input_number += 1

# 3-4-3
input_number = int(input("Nhập số bắt đầu: "))
output_number = int(input("Nhập số kết thúc: "))
while input_number <= output_number:
        input_number += 1
        if input_number % 2 == 0:
            print(f"Đây là số chẵn thứ {input_number}")


# 3-4-4
# Cách 1
juices_menu = ['táo', 'xoài', 'chuối']
juices_price = [10, 20, 30]

i = 0
while i < len(juices_menu):
    print(juices_menu[i], "--", juices_price[i])
    i += 1

# Cách 2
juices_menu_and_price = ["táo", 10, "xoài", 20, "chuối", 30]

i = 0
while i <= 5:
    print(juices_menu_and_price[i], "--", juices_menu_and_price[i+1])
    i += 2

# Cách 3
juices_menu_and_price = ["táo", "xoài", "chuối", 10, 20, 30]

i = 0
while i < 3:
    print(juices_menu_and_price[i], "--", juices_menu_and_price[i+3])
    i += 1


# 3-4-5
juices_name = ["táo", "xoài", "chuối"]
print(f"Danh sách đồ uống: {juices_name}")

juices_menu = ["táo", "xoài", "chuối", 10, 20, 30]
print("Danh sách đồ uống nước trái cây:")
i = 0
while i < 3:
    print(f"{juices_menu[i]} : {juices_menu[i+3]}")
    i += 1

# 3-4-6
juices_name = ["táo", "xoài", "chuối"]
i = 0
while i < 3:
    print(juices_name[i], end = " ")
    i += 1

juices_menu = ["táo", "xoài", "chuối", 10, 20, 30]
print("\nDanh sách đồ uống nước trái cây:")
i = 0
while i < 3:
    print(f"{juices_menu[i]} : {juices_menu[i+3]}")
    i += 1


# 3-4-7
juices_name = ["táo", "xoài", "chuối"]
i = 0
while i < 3:
    print(juices_name[i], end = "\t")
    i += 1

juices_menu = ["táo", "xoài", "chuối", 10, 20, 30]
print("\nDanh sách đồ uống nước trái cây:")
i = 0
while i < 3:
    print(f"{juices_menu[i]} : {juices_menu[i+3]}")
    i += 1


# 3-4-8 (Cuối slide): Làm lại bài tập hw31 với for và break
# HW31
# Khởi tạo một danh sách bao gồm các phần tử là điểm của của một sinh viên (hệ 10). Hãy thực hiện:
# Tạo một danh sách là các điểm chữ tương ứng với điểm hệ 10 ở trên.
# Tính điểm trung bình hệ 10 và hệ 4


def convert_to_grade(diem):
    if diem < 4:
        return "F", 0
    elif diem < 5:
        return "D", 1
    elif diem < 5.5:
        return "D+", 1.5
    elif diem < 6.5:
        return "C", 2
    elif diem < 7:
        return "C+", 2.5
    elif diem < 8:
        return "B", 3
    elif diem < 8.5:
        return "B+", 3.5
    elif diem < 9:
        return "A", 4
    else:
        return "A+", 4

print("Yêu cầu nhập đủ điểm của 9 môn")
diem_he_10 = input("Nhập điểm 9 môn cách nhau bởi dấu phẩy: ").split(", ")
diem_trung_binh_he_10 = 0
if len(diem_he_10) != 9:
    print("Nhập sai hoặc thiếu điểm")
else:
    diem_he_4_total = 0
    for i in diem_he_10:
        if i.isdigit():
            continue
        elif not i.isdigit():
            print("Điểm không hợp lệ")
            break
        diem = float(i)
        diem_chu, diem_he_4 = convert_to_grade(diem)
        print(f"Điểm chữ: {diem_chu}, Điểm hệ 4: {diem_he_4}")
        diem_he_4_total += diem_he_4
    else:
        for x in diem_he_10:
            diem_trung_binh_he_10 += float(x) / 9
        diem_trung_binh_he_4 = diem_he_4_total / 9
        print(f"Điểm trung bình hệ 10: {diem_trung_binh_he_10}, Điểm trung bình hệ 4: {diem_trung_binh_he_4}")


        












































