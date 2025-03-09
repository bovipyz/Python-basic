# Viết chương trình nhập vào m điểm (toán, lý, hóa, anh, văn) của n sinh viên trong một lớp.
# ví dụ:
# SV1 = [2, 3, 1, 8, 10]
# SV2 = [6, 6, 5, 8, 1]
# SV3 = [9, 7, 10, 10, 10]
# SV4 = [2, 7, 10, 5, 10]
# Tính điểm trung bình của mỗi sinh viên và in ra kết quả màn hình.

# for
numbers_student = int(input("Nhập số lượng sinh viên: "))
for i in range(numbers_student):
    points = []
    studens_points = []
    input_math = float(input(f"Nhập điểm toán của sinh viên thứ {i + 1}: "))
    if input_math < 0 or input_math > 10:
        print("Điểm không hợp lệ!")
        break
    studens_points.append(input_math)
    points.append(["toán", input_math])
    input_physics = float(input(f"Nhập điểm lý của sinh viên thứ {i + 1}: "))
    if input_physics < 0 or input_physics > 10:
        print("Điểm không hợp lệ!")
        break
    studens_points.append(input_physics)
    points.append(["Lý", input_physics])
    input_chemistry = float(input(f"Nhập điểm hóa của sinh viên thứ {i + 1}: "))
    if input_chemistry < 0 or input_chemistry > 10:
        print("Điểm không hợp lệ!")
        break  
    studens_points.append(input_chemistry)
    points.append(["hóa", input_chemistry])
    input_english = float(input(f"Nhập điểm anh của sinh viên thứ {i + 1}: "))
    if input_english < 0 or input_english > 10:
        print("Điểm không hợp lệ!")
        break 
    studens_points.append(input_english)
    points.append(["anh", input_english])
    input_literature = float(input(f"Nhập điểm văn của sinh viên thứ {i + 1}: "))
    if input_literature < 0 or input_literature > 10:
        print("Điểm không hợp lệ!")
        break 
    studens_points.append(input_literature)
    points.append(["văn", input_literature])

    total = 0
    for x in studens_points:
        total += x
        average = total / 5
    print(f"Danh sách điểm toán, lý, hóa, anh, văn của sinh viên thứ {i + 1}:\n{points}")
    print(f"Điểm trung bình của sinh viên thứ {i + 1} là: {average}")

print("Kết thúc chương trình")


# while 1
continue_program = "có"

while continue_program == "có":
    i = 0
    numbers_student = int(input("Nhập số lượng sinh viên: "))
    while i < numbers_student:
        points = list(map(float, input(f"Nhập điểm toán, lý, hóa, anh, văn của sinh viên thứ {i+1}: ").split(", ")))
        if len(points) != 5:
            print("Bạn đã nhập sai số lượng điểm, vui lòng nhập lại")
        elif len(points) == 5:
            for x in points:
                if x < 0 or x > 10:
                    print("Điểm không hợp lệ, hãy nhập lại")
                    break
            else:
                print(f"Danh sách điểm toán, lý, hóa, anh, văn của sinh viên thứ {i+1}:\n{points}")
                average = sum(points) / 5
                print(f"Điểm trung bình của sinh viên thứ {i + 1} là {average}")
                i += 1
    continue_program = input("Bạn có muốn nhập tiếp không? (Có/Không)\n").lower()
    if continue_program != "có":
        break
print("Kết thúc chương trình")


# while 2
continue_program = "có"
while continue_program:
    i= 0
    numbers_student = int(input("Nhập số lượng sinh viên: "))
    while i < numbers_student:
        points = []
        studens_points = []
        input_math = float(input(f"Nhập điểm toán của sinh viên thứ {i + 1}: "))
        while input_math < 0 or input_math > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại điểm toán.")
            input_math = float(input(f"Nhập điểm toán của sinh viên thứ {i + 1}: "))
        studens_points.append(input_math)
        points.append(["toán", input_math])
        input_physics = float(input(f"Nhập điểm lý của sinh viên thứ {i + 1}: "))
        while input_physics < 0 or input_physics > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại điểm lý.")
            input_physics = float(input(f"Nhập điểm lý của sinh viên thứ {i + 1}: "))
        studens_points.append(input_physics)
        points.append(["Lý", input_physics])
        input_chemistry = float(input(f"Nhập điểm hóa của sinh viên thứ {i + 1}: "))
        while input_chemistry < 0 or input_chemistry > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại điểm hóa.")
            input_chemistry = float(input(f"Nhập điểm hóa của sinh viên thứ {i + 1}: "))
        studens_points.append(input_chemistry)
        points.append(["hóa", input_chemistry])
        input_english = float(input(f"Nhập điểm anh của sinh viên thứ {i + 1}: "))
        while input_english < 0 or input_english > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại điểm anh.")
            input_english = float(input(f"Nhập điểm anh của sinh viên thứ {i + 1}: "))
        studens_points.append(input_english)
        points.append(["anh", input_english])
        input_literature = float(input(f"Nhập điểm văn của sinh viên thứ {i + 1}: "))
        while input_literature < 0 or input_literature > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại điểm văn.")
            input_literature = float(input(f"Nhập điểm văn của sinh viên thứ {i + 1}: "))
        studens_points.append(input_literature)
        points.append(["văn", input_literature])

        total = 0
        for x in studens_points:
            total += x
            average = total / 5
        print(f"Danh sách điểm toán, lý, hóa, anh, văn của sinh viên thứ {i+1}:\n{points}")
        print(f"Điểm trung bình của sinh viên thứ {i + 1} là: {average}")
        i += 1
    continue_program = input("Bạn có muốn nhập tiếp không? (Có/không)\n").lower()
    if continue_program != "có":
        continue_program = False
        # break

print("Kết thúc chương trình")






