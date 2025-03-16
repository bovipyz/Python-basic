# 3-5-6
# Sinh viên xây dựng hàm cho phép người dùng nhập thêm 1 đồ uống vào menu

def input_name_price():
    drinks = {}
    input_drink = input("Nhập tên đồ uống: ")
    input_price = int(input('Nhập giá: '))
    drinks[input_drink] = input_price
    print(drinks)
    return 

input_name_price()

# 3-5-6: Xây dựng hàm tính số phần từ của một danh sách
def count():
    list = []
    input_numbers = int(input("Nhập vào một số: "))
    for i in range(input_numbers + 1):
        list.append(i)
    print(len(list))
    return

count()

# 3-5-6: Xây dựng hàm kiểm tra giá trị nhập vào phải nằm trong một khoảng nhất định
def check(point):
    min = int(input("Nhập vào giới hạn nhỏ nhất: "))
    max = int(input("Nhập vào giới hạn lớn nhất: "))
    if min <= input_math and  input_math <= max:
        return True
    else:
        return False
input_math = int(input("Nhập vào điểm toán: "))
print(f"Kiểm tra số điểm nhập vào: {check(input_math)}")

# 3-5-6: Xây dựng hàm sắp xếp một danh sách lưu các số theo thứ tự từ lớn đến nhỏ hoặc ngược lại

def sort_reverse(input_number):
    input_number.sort()
    print(f"Danh sách sau khi sắp xếp {input_numbers}")
    input_number.reverse()
    print(f"Danh sách sau khi sắp xếp và đảo ngược {input_numbers}")
    return input_number

input_numbers = list(map(int, input("Nhập vào một dãy số ngẫu nhiên: ").split(",")))
sort_reverse(input_numbers)

# bài toán 4-3: Xây dựng hàm chuyển đổi giá trị của 2 list vào trong 1 đối tượng dictionary
dic = {}
def change(subject, grade):
    for i in range(len(subject)):
        dic[subject[i]] = grade[i]
    return dic


input_numbers = int(input("Nhập vào một số môn học: "))
subjects = []
grades = []
for i in range(input_numbers):
    input_subject = input(f"Nhập tên môn thứ {i + 1}: ")
    subjects.append(input_subject)
    input_grade = int(input(f"Nhập vào điểm môn thứ {i + 1}: "))
    grades.append(input_grade)

print(f"Danh sách trước khi gộp: {subjects}\n{grades}")
print(f"Danh sách sau khi gộp: {change(subjects, grades)}")

# Thực hành 4.4: XÂY DỰNG CHƯƠNG TRÌNH BÁN HÀNG
# Xây dựng 1 biến lưu thông tin của hàng hóa và giá bán (4 loại hàng hóa)
# Xây dựng hàm in ra màn hình các mặt hàng và giá bán
# Xây dựng hàm hỏi người dùng muốn mua sản phẩm nào và lưu các mặt hàng đã mua vào giỏ hàng
# Xây dựng hàm tính tiền các mặt hàng trong giỏ hàng và in ra hóa đơn
# Chạy các hàm theo thứ tự từ trên xuống

items = {
    "hải sản":{
        "tôm": 1,
        "ghẹ": 2,
        "cua": 3,
        "ốc": 4,
        "mực": 5
    },
    "rau":{
        "muống": 6,
        "cải": 7,
        "súp lơ": 8,
        "ngót": 9
    },
    "thịt":{
        "trâu": 10,
        "bò": 11,
        "lợn": 12,
        "gà": 13,
        "vịt": 14
    },
    "nước":{
        "muối": 15,
        "tương": 16,
        "ngọt": 17,
        "xốt": 18
    }
}

def printf():
    for item in items:
        print(f"Thông tin về các mặt hàng: {item}")
        for info in items[item]:
            print(f"{info} -- {items[item][info]}") 


store = {} 
def buy_store():
    while True:
        category_choice = input("Bạn muốn mua mặt hàng từ nhóm nào?\n")
        if category_choice in items:
            print(f"Chọn các mặt hàng trong nhóm {category_choice}:")
            for item in items[category_choice]:
                print(item)
            buy_item = input(f"Bạn muốn mua món gì từ nhóm {category_choice}?\n")
            if buy_item in items[category_choice]:
                input_number = int(input("Nhập số lượng muốn mua: "))
                store[buy_item] = input_number
            else:
                print("Món này không có trong nhóm.")
        else:
            print("Nhóm mặt hàng không hợp lệ.")
        continue_program = input("Bạn có muốn mua tiếp không? (Có/không)\n")
        if continue_program != "có":
            break
    return print(f"Các mặt hàng đã chọn: {store}")



def purchase():
    results = 0
    for info in store:
        for item in items:
            if info in items[item]:
                price = items[item][info]
                value = store[info]
                results += price * value   
    return print(f"Tổng hóa đơn: {results}")

printf()
buy_store()
purchase()

# BÀI TẬP HW4 – 3
# Xây dựng hàm nhập số sinh viên, nhập số môn học
# Xây dựng hàm cho phép người dùng nhập dữ liệu về sinh viên và điểm vào một dictionary
# Điểm trung bình từ điểm đầu vào được lưu trong một dictionary và lưu ngược lại vào dictionary
# Xây dựng hàm in thông tin của sinh viên được chứa trong dictionary ở trên ra màn hình
# Chạy các hàm theo thứ tự từ trên xuống

dic_students_points = []

def input_info(input_numbers):
    for number in range(input_numbers):
        student = {}  
        input_ID = int(input(f"Nhập id của sinh viên thứ {number + 1}: "))
        input_name = input(f"Nhập tên sinh viên thứ {number + 1}: ")
        input_subjects = int(input(f"Nhập số môn học của sinh viên thứ {number + 1}: "))
        student["ID"] = input_ID
        student["name"] = input_name
        student["num_subjects"] = input_subjects
        dic_students_points.append(student)  
        print(f"Thông tin sinh viên thứ {number + 1}")
        print(f"Sinh viên ID: {student['ID']}")
        print(f"Tên sinh viên: {student['name']}")
        print(f"Tổng số môn học của sinh viên thứ {number + 1}: {student['num_subjects']} môn")
    return

def input_grade():
    for student in dic_students_points: 
        subjects = {}
        total_points = 0
        num_subjects = student["num_subjects"] 

        for i in range(num_subjects):
            input_points = float(input(f"Nhập điểm môn học thứ {i + 1} cho sinh viên {student['name']}: "))
            subjects[f"Điểm môn thứ {i + 1}"] = input_points
            total_points += input_points
        
        average = total_points / num_subjects if num_subjects > 0 else 0 

        student["subjects"] = subjects
        student["average"] = average

        print(f"Điểm học phần của {student['name']}: {student['subjects']}")
        print(f"Điểm trung bình của {student['name']}: {student['average']}")
    
    return dic_students_points

input_numbers = int(input("Nhập số lượng sinh viên: "))
input_info(input_numbers)
input_grade()


###########
###########
def input_info(numbers):
    dic_students_points = {}
    subjects = {}
    for number in range(numbers):
        input_ID = int(input(f"Nhập id của sinh viên thứ {number + 1}: "))
        input_name = input(f"Nhập tên sinh viên thứ {number + 1}: ")
        input_subjects = int(input(f"Nhập số môn học của sinh viên thứ {number + 1}: "))
        result = 0
        for i in range(input_subjects):
            input_name = input(f"Nhập tên môn học thứ {i + 1}: ")
            input_points = float(input(f"Nhập điểm môn học thứ {i + 1}: "))
            result += input_points
            average = result / input_subjects
            dic_students_points["ID"] = input_ID
            dic_students_points["name"] = input_name
            subjects[input_name] = input_points
            dic_students_points["subjects"] = subjects
            dic_students_points["average"] = average
        print(f"Thông tin sinh viên thứ {number + 1}")
        print(f"Sinh viên ID: {dic_students_points["ID"]}")
        print(f"Tên sinh viên: {dic_students_points["name"]}")
        print(f"Điểm học phần: {dic_students_points["subjects"]}")
        print(f"Điểm trung bình: {dic_students_points["average"]}")
    return dic_students_points

input_numbers = int(input("Nhập số lượng sinh viên: "))
input_info(input_numbers)






























