# Viết chương trình chat bot cho phép người dùng hỏi các câu hỏi và máy tính trả lời
# Nếu câu trả lời chưa được lập trình thì in ra thông báo: “Xin lỗi tôi không biết trả lời thế nào”


# import webbrowser

# user_input = input("Hãy nhập từ khóa google để hỏi: ").lower()
# if user_input == "google":
#     webbrowser.open("https://www.google.com")
#     print("Đang mở trang Google...")
# else:
#     print("Xin lỗi tôi không biết trả lời thế nào")


# Cách 1: Dùng if
user_input = input("Nhập phép toán có hai chữ số nguyên: ")
# Cộng
if "+" in user_input:
    numbers = user_input.split("+")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isalpha() or num2.isalpha():
            print("Xin lỗi tôi không biết trả lời thế nào")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 + num2
            print(f"Kết quả: {result}")
    if len(numbers) != 2:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Trừ
if "-" in user_input:
    numbers = user_input.split("-")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isalpha() or num2.isalpha():
            print("Xin lỗi tôi không biết trả lời thế nào")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 - num2
            print(f"Kết quả: {result}")
    if len(numbers) != 2:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Nhân
if "*" in user_input:
    numbers = user_input.split("*")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isalpha() or num2.isalpha():
            print("Xin lỗi tôi không biết trả lời thế nào")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 * num2
            print(f"Kết quả: {result}")
    if len(numbers) != 2:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Chia
if "/" in user_input:
    numbers = user_input.split("/")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isalpha() or num2.isalpha():
            print("Xin lỗi tôi không biết trả lời thế nào")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if num2 == 0:
                print("Không thể chia cho 0!")
            if num2 != 0:
                result = num1 / num2
                print(f"Kết quả: {result}")
    if len(numbers) != 2:
        print("Xin lỗi tôi không biết trả lời thế nào")
if "+" not in user_input and "-" not in user_input and "*" not in user_input and "/" not in user_input:
    print("Xin lỗi tôi không biết trả lời thế nào")


# Cách 2: Dùng if, else
user_input = input("Nhập phép toán có hai chữ số nguyên: ")

# Cộng
if "+" in user_input:
    numbers = user_input.split("+")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 + num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Trừ
if "-" in user_input:
    numbers = user_input.split("-")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 - num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Nhân
if "*" in user_input:
    numbers = user_input.split("*")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 * num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Chia
if "/" in user_input:
    numbers = user_input.split("/")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isalpha() or num2.isalpha():
            print("Xin lỗi tôi không biết trả lời thế nào")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if num2 == 0:
                print("Không thể chia cho 0!")
            else:
                result = num1 / num2
                print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")
if "+" not in user_input and "-" not in user_input and "*" not in user_input and "/" not in user_input:
    print("Xin lỗi tôi không biết trả lời thế nào")


# Cách 3: Dùng if, elif, else
user_input = input("Nhập phép toán có hai chữ số nguyên: ")

# Cộng
if "+" in user_input:
    numbers = user_input.split("+")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1) 
            num2 = int(num2)
            result = num1 + num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Trừ
elif "-" in user_input:
    numbers = user_input.split("-")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 - num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Nhân
elif "*" in user_input:
    numbers = user_input.split("*")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            result = num1 * num2
            print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")

# Chia
elif "/" in user_input:
    numbers = user_input.split("/")
    if len(numbers) == 2:
        num1 = numbers[0].strip()
        num2 = numbers[1].strip()
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if num2 == 0:
                print("Không thể chia cho 0!")
            else:
                result = num1 / num2
                print(f"Kết quả: {result}")
        else:
            print("Xin lỗi tôi không biết trả lời thế nào")
    else:
        print("Xin lỗi tôi không biết trả lời thế nào")
else:
    print("Xin lỗi tôi không biết trả lời thế nào")















































