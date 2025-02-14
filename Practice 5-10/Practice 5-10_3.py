# Chương trình tính chỉ số BMI = cân nặng (kg) / Chiều cao^2 (m) 

Height = float(input("Nhập chiều cao (m) của bạn: "))
Weight = float(input("Nhập vào cân nặng (kg) của bạn: "))
BMI_index = Weight / Height**2 
print(f"Kết quả {BMI_index} kg/m^2")