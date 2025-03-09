# Cho phép người dùng nhập vào chiều cao của các bạn trong lớp.
# Hiển thị chiều cao của sinh viên cao nhất – thấp nhất trong lớp
# Tính chiều cao trung bình của sinh viên trong lớp.
# Số lượng sinh viên trong lớp có chiều cao lớn hơn hoặc bằng chiều cao trung bình của lớp


# for
height_students = []
numbers_student = int(input("Nhập số lượng học sinh: "))
for i in range(numbers_student):
    height_input = float(input(f"Nhập vào chiều cao học sinh thứ {i + 1}: "))
    height_students.append(height_input)
for i in range(len(height_students)):
    if height_students[i] <= 0 or height_students[i] >= 2:
        print(f"Chiều cao của sinh viên {i + 1} không phù hợp")
        break
    else:
        print(f"Chiều cao của sinh viên thứ {i + 1} là: {height_students[i]} (m)")
else:
    print(f"Tổng số sinh viên trong lớp: {len(height_students)}")
    # print(f"Chiều cao của các sinh viên là: \n{height_students}")
    print(f"Sinh viên cao nhất trong lớp: {max(height_students)} (m)")
    print(f"Sinh viên thấp nhất trong lớp: {min(height_students)} (m)")
    sum_heights = sum(height_students)
    average_height = sum_heights / len(height_students)
    print(f"Chiều cao TB của sinh viên: {average_height} (m)")
    count_above_or_equal_average = 0
    for i in height_students:
        if i >= average_height:
            count_above_or_equal_average += 1
    print(f"Số sinh viên có chiều cao >= chiều cao TB là: {count_above_or_equal_average}")


# while
while True:
    i = 0
    height_students = []
    numbers_student = int(input("Nhập số lượng học sinh: "))
    for i in range(numbers_student):
        while True:
            height_input = float(input(f"Nhập vào chiều cao học sinh thứ {i + 1}: "))
            if height_input <= 0 or height_input >= 2:
                print(f"Chiều cao của sinh viên thứ {i + 1} không phù hợp, vui lòng nhập lại")
            else:
                height_students.append(height_input)
                i += 1
                break
    else:
        print(f"Tổng số sinh viên trong lớp: {len(height_students)}")
        print(f"Sinh viên cao nhất trong lớp: {max(height_students)} (m)")
        print(f"Sinh viên thấp nhất trong lớp: {min(height_students)} (m)")
        sum_heights = sum(height_students)
        average_height = sum_heights / len(height_students)
        print(f"Chiều cao TB của sinh viên: {average_height} (m)")
        count_above_or_equal_average = 0
        for i in height_students:
            if i >= average_height:
                count_above_or_equal_average += 1
        print(f"Số sinh viên có chiều cao >= chiều cao TB là: {count_above_or_equal_average}")
    continue_program = input("Bạn có muốn nhập tiếp không? (Có/Không)\n")
    if continue_program != "có":
        break
print("Kết thúc chương trình")





















































