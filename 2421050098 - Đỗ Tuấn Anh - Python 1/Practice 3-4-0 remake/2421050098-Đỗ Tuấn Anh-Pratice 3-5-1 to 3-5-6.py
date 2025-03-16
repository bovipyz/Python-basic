# # 3-5-1
# # Tạo một biến dictionary lưu trữ tên và giá đồ uống của một cửa hang trà chanh
# # In menu của quán ra màn hình

# juices_price = {
#   "chanh": 10,
#   "trà": 20,
#   "đào": 30,
#   "cam": 40,
#   "quất": 50
# }
# print(f"Danh sách các loại đồ uống\n{juices_price}")


# # 3-5-2
# # Tạo một biến dictionary lưu trữ tên và giá đồ uống của một cửa hang trà chanh
# # In menu của quán ra màn hình

# juices_price = {
#   "chanh": 10,
#   "trà": 20,
#   "đào": 30,
#   "cam": 40,
#   "quất": 50
# }
# print("Danh sách các loại đồ uống")
# # for key in juices_price:
# #   print(f"{key}: {juices_price[key]}")
# for key, values in juices_price.items():
#   print(f"{key}: {values}")


# # 3-5-3
# # Hỏi người dùng số lượng đồ uống mới thêm vào
# # Cho phép người dùng thêm số lượng món mới vào trong menu

# drinks_name = {}
# while True:
#   i = 0
#   input_number = int(input("Nhập số lượng đồ uống muốn thêm vào: "))
#   while i < input_number:
#     input_drink = input(f"Nhập tên đồ uống thứ {i + 1}: ")
#     input_price = int(input(f"Nhập giá đồ uống thứ {i + 1}: "))
#     drinks_name[input_drink] = input_price
#     i += 1
#   print(f"Danh sách đồ uống sau khi thêm\n{drinks_name}")
#   continue_program = input("Bạn có muốn nhập tiếp không? (Có/Không)\n").lower()
#   if continue_program != "có":
#     break
# print("Kết thúc chương trình")


# # 3-5-4
# # Tổ chức lại biến lưu menu của quán
# # Chia các món đồ uống của quán ra làm các loại khác nhau (ví dụ: nước hoa quả, trà, sinh tố)
# # In menu của quán ra màn hình theo từng nhóm đồ uống

# menu_shop = {
#   "fruis_juice": {
#     "nho": 10,
#     "xoài": 20,
#     "cam": 30
#   },
#   "tea": {
#     "đào": 11,
#     "tắc": 12,
#     "đá": 13
#   },
#   "smoothie": {
#     "táo": 21,
#     "dâu": 22,
#     "kiwi": 23
#   }
# }

# for type in menu_shop:
#   print(f"Thông tin về {type}")
#   for infor in menu_shop[type]:
#     print(f"{infor}: {menu_shop[type][infor]}")


# # 3-5-5
# # Cho phép sinh viên nhập điểm 3 môn Toán, Lý và Hóa của mình
# # Tính tổng điểm của sinh viên, sau đó so sánh với điểm chuẩn của từng ngành
# # CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15
# # In kết quả xem người dùng đã trúng tuyển mấy ngành và liệt kê tên các ngành đã trúng tuyển

# industry_benchmarks = {
#   "CNTT chất lượng cao": 22,
#   "CNTT": 18,
#   "KHDL": 18,
#   "Địa chất": 17,
#   "Môi trường": 15
# }
# pass_industry = {}
# input_math = float(input("Nhập điểm toán: "))
# input_physics = float(input("Nhập điểm vậy lý: "))
# input_chemistry = float(input("Nhập điểm hóa: "))
# total = input_math + input_physics + input_chemistry

# for point in industry_benchmarks:
#   if total >= industry_benchmarks[point]:
#     pass_industry[point] = industry_benchmarks[point]
# if pass_industry:
#     print(f"Danh sách các ngành đã trúng tuyển: {pass_industry}")
# else:
#     print("Bạn không trúng tuyển ngành nào")


# 3-5-6
# Viết chương trình nhập vào n sinh viên, nhập thông tin của sinh viên và điểm của m môn học của môi sinh viên
# Tính điểm trung bình của mỗi sinh viên và in kết quả ra màn hình.

# input_number = int(input("Nhập vào số lượng sinh viên: "))
students_list = []

while True:
  # students_list = []
  total = 0
  input_number = int(input("Nhập vào số lượng sinh viên: "))
  for i in range(input_number):
    # students_list = []
    input_id = int(input(f"Nhập số id của sinh viên thứ {i + 1}: "))
    input_name = input("Nhập tên sinh viên: ")

    input_subjects = int(input(f"Nhập số môn học của sinh viên thứ {i + 1}: "))

    credit = {}
    total = 0

    # python = float(input("Nhập điểm môn python: "))
    # credit["python"] = python
    # web = float(input("Nhập điểm môn web: "))
    # credit["web"] = web
    # english = float(input("Nhập điểm môn tiếng anh: "))
    # credit["english"] = english
    # total = web + english + python

    for s in range(input_subjects):
      input_point = float(input(f"Nhập điểm môn thứ {s + 1}: "))
      credit[f"Môn thứ {s + 1}"] = input_point
      total += input_point

    average = total / len(credit) 
    students_list.append({
      "id": input_id,
      "name": input_name,
      "grades_list": credit,
      "average": average
    })
    print(f"Thông tin của sinh viên thứ {i + 1}: {students_list[-1]}")
    print(f"Điểm trung bình của sinh viên thứ {i + 1}: {average}")
  continue_program = input("Bạn có muốn nhập thêm sinh viên không? (Có/Không): ").lower()
  if continue_program != 'có':
    break
print(f"Danh sách sinh viên\n{students_list}\n")
print("Danh sách sinh viên và điểm trung bình:")
for student in students_list:
  print(f"Sinh viên ID: {student['id']}, Tên: {student['name']}, Điểm trung bình: {student['average']}")








































