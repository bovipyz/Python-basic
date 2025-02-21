# Chương trình in ra câu chào theo tên người dùng

my_name = input("Nhập tên của bạn: ")
print(f"Hello {my_name}")

# Chương trình hỏi người dùng muốn mua bao nhiêu ly trà sữa trân châu đường đen, sau đó in ra hóa đơn

my_dict = {"Trà sữa trân châu đường đen": 30}
print("Bạn muốn mua bao nhiêu ly trà sữa trân châu đường đen?")
number = int(input("Vui lòng nhập số lượng: "))
total = my_dict["Trà sữa trân châu đường đen"] * number
print(f"Tổng tiền phải trả là: {total} nghìn đồng (vnđ)")

# Chương trình tính chỉ số BMI = cân nặng (kg) / Chiều cao^2 (m) 

Height = float(input("Nhập chiều cao (m) của bạn: "))
Weight = float(input("Nhập vào cân nặng (kg) của bạn: "))
BMI_index = Weight / Height**2 
print(f"Kết quả {BMI_index} kg/m^2")


























