# Cho phép người dùng nhập vào chiều cao của các bạn trong lớp.
# Hiển thị chiều cao của sinh viên cao nhất – thấp nhất trong lớp
# Tính chiều cao trung bình của sinh viên trong lớp.
# Số lượng sinh viên trong lớp có chiều cao lớn hơn hoặc bằng chiều cao trung bình của lớp


height_students = [1.65, 1.7, 1.55, 1.64, 1.78, 1.67, 1.59, 1.62, 1.45, 1.8, 1.69, 1.5]
print("Tổng số sinh viên trong lớp: 12")
print(f"Chiều cao của các sinh viên là: \n{height_students}")
print(f"Sinh viên cao nhất trong lớp: {max(height_students)} (m)")
print(f"Sinh viên thấp nhất trong lớp: {min(height_students)} (m)")
sum_heights = sum(height_students)
average_height = sum_heights / len(height_students)
print(f"Chiều cao TB của sinh viên: {average_height} (m)")
count_above_or_equal_avg = 0
for i in height_students:
    if i >= average_height:
        count_above_or_equal_avg += 1
print(f"Số sinh viên có chiều cao >= chiều cao TB là: {count_above_or_equal_avg}")




















































