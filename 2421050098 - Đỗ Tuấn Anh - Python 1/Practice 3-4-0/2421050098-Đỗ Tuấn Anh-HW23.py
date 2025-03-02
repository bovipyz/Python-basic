# Viết chương trình nhập vào m điểm (toán, lý, hóa, anh, văn) của n sinh viên trong một lớp.
# ví dụ:
# SV1 = [2, 3, 1, 8, 10]
# SV2 = [6, 6, 5, 8, 1]
# SV3 = [9, 7, 10, 10, 10]
# SV4 = [2, 7, 10, 5, 10]
# Tính điểm trung bình của mỗi sinh viên và in ra kết quả màn hình.


numbers_student = int(input("Nhập số lượng sinh viên: "))
for i in range(numbers_student ):
    points = list(map(float, input(f"Nhập điểm toán, lý, hóa, anh, văn của sinh viên thứ {i+1}: ").split(", ")))
    if len(points) != 5:
        print("Bạn đã nhập sai số lượng điểm")
    elif len(points) == 5:
        for x in points:
            if x < 0 or x > 10:
                print("Điểm không hợp lệ")
                break
        else:
            average = sum(points) / 5
            print(f"Điểm trung bình của sinh viên thứ {i + 1} là {average}")
