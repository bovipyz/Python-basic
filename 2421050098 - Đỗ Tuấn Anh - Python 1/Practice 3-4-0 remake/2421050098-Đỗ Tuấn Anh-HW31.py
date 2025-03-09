# Khởi tạo một danh sách bao gồm các phần tử là điểm của của một sinh viên (hệ 10). Hãy thực hiện:
# Tạo một danh sách là các điểm chữ tương ứng với điểm hệ 10 ở trên.
# Tính điểm trung bình hệ 10 và hệ 4

# for
numbers = int(input("Nhập số lượng sinh viên: "))
for n in range(numbers):
    list_subjects = []
    points = []
    subjects = int(input(f"Nhập số môn của sinh viên thứ {n + 1}: "))
    print(f"Sinh viên thứ {n + 1}")
    for s in range(subjects):
        input_subject = int(input(f"Nhập điểm môn thứ {s + 1}: "))
        list_subjects.append([f"Môn thứ {s + 1}", input_subject])
        points.append(input_subject)
    diem_trung_binh_he_10 = 0
    diem_he_4_total = 0
    for i in range(subjects):
        p = points[i]
        if p < 4:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: F, Điểm hệ 4: 0")
            diem_he_4_total += 0
        elif p < 5:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: D, Điểm hệ 4: 1")
            diem_he_4_total += 1
        elif p < 5.5:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: D+, Điểm hệ 4: 1.5")
            diem_he_4_total += 1.5
        elif p < 6.5:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: C, Điểm hệ 4: 2")
            diem_he_4_total += 2
        elif p < 7:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: C+, Điểm hệ 4: 2.5")
            diem_he_4_total += 2.5
        elif p < 8:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: B, Điểm hệ 4: 3")
            diem_he_4_total += 3
        elif p < 8.5:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: B+, Điểm hệ 4: 3.5")
            diem_he_4_total += 3.5
        elif p < 9:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: A, Điểm hệ 4: 4")
            diem_he_4_total += 4
        else:
            print(f"Môn thứ {i + 1}, Điểm hệ 10: {p}, Điểm chữ: A+, Điểm hệ 4: 4")
            diem_he_4_total += 4
            
        diem_trung_binh_he_10 += p
    average_10_points = diem_trung_binh_he_10 / subjects
    average_4_points = diem_he_4_total / len(points)
    print(f"Điểm trung bình hệ 10: {average_10_points}")
    print(f"Điểm trung bình hệ 4: {average_4_points}")


# while 
ten_point_system = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
word_point_system = ["B+", "C+", "B", "F", "A+", "C", "C", "A+", "B+"]
four_point_system = [3.5, 2.5, 3.0, 0, 4.0, 2.0, 2.0, 4.0, 3.5]
print("----------Điểm trung bình----------")

i = 0
total = 0
while i < len(ten_point_system):
    total += ten_point_system[i]
    i += 1
average = total / len(ten_point_system)
print(f"Điểm trung bình hệ 10: {average}")
i = 0
total = 0
while i < len(four_point_system):
    total += four_point_system[i]
    i += 1
average = total / len(ten_point_system)
print(f"Điểm trung bình hệ 4: {average}")


















































