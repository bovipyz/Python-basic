# Chương trình hỏi người dùng muốn mua bao nhiêu ly trà sữa trân châu đường đen, sau đó in ra hóa đơn

my_dict = {"Trà sữa trân châu đường đen": 30}
print("Bạn muốn mua bao nhiêu ly trà sữa trân châu đường đen?")
number = int(input("Vui lòng nhập số lượng: "))
total = my_dict["Trà sữa trân châu đường đen"] * number
print(f"Tổng tiền phải trả là: {total} nghìn đồng (vnđ)")