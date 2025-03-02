# Khởi tạo một danh sách bao gồm các phần tử là điểm của của một sinh viên (hệ 10). Hãy thực hiện:
# Tạo một danh sách là các điểm chữ tương ứng với điểm hệ 10 ở trên.
# Tính điểm trung bình hệ 10 và hệ 4


ten_point_system = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
word_point_system = ["B+", "C+", "B", "F", "A+", "C", "C", "A+", "B+"]
four_point_system = [3.5, 2.5, 3.0, 0, 4.0, 2.0, 2.0, 4.0, 3.5]
print("----------Điểm trung bình----------")

print(f"Tổng số môn học: {len(ten_point_system)}")
total = 0
for i in ten_point_system:
    total += i
total = total / len(ten_point_system)
print(f"Điểm trung bình hệ 10: {total}")

total = 0
for i in four_point_system:
    total += i
total = total / len(four_point_system)
print(f"Điểm trung bình hệ 4: {total}")















































