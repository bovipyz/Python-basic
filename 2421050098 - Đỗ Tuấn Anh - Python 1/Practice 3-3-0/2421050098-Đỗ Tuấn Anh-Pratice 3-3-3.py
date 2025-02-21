# Lưu giá tiền của 5 loại đồ uống
# Cho phép người dùng chọn 1 trong 5 loại đồ uống và số lượng muốn order
# Nếu đồ uống có trong menu thì in hóa đơn ra màn hình

# menu_fruits_juice = {
#     "cam": 10,
#     "táo": 20,
#     "xoài": 30,
#     "chuối": 40,
#     "nho": 50
# }
# print(f"Danh sách nước trái cây: {menu_fruits_juice}")
# choice = input("Hãy nhập vào loại nước trái cây bạn muốn: ").lower()
# if choice in menu_fruits_juice:
#     quantity = int(input(f"Nhập vào số lượng bạn muốn mua: "))
#     if quantity < 0:
#         print("Số không phù hợp")
#     else:
#         total = menu_fruits_juice[choice] * quantity
#         print(f"Tổng bạn phải trả là: {total}$")
# else:
#     print("Không có trong danh sách")






# Lập một danh sách
juice_1 = "cam" 
price_1 = 10 
juice_2 = "táo" 
price_2 = 20
juice_3 = "xoài"
price_3 = 30
juice_4 = "chuối" 
price_4 = 40
juice_5 = "nho" 
price_5 = 50
list = [juice_1, juice_2, juice_3, juice_4, juice_5]
print(f"Danh sách nước trái cây: {juice_1}: {price_1}, {juice_2}: {price_2}, {juice_3}: {price_3}, {juice_4}: {price_4}, {juice_5}: {price_5}")


# Cách 1: Dùng if
choice = input("Hãy nhập loại nước trái cây bạn muốn: ").lower()
if choice in list:
    if choice == "cam":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:                                        
            print("Số không phù hợp")   
        if quantity >= 0:
            total = quantity * price_1
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "táo":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        if quantity >= 0:
            total = quantity * price_2
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "xoài":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        if quantity >= 0:
            total = quantity * price_3
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "chuối":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        if quantity >= 0:
            total = quantity * price_4
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "nho":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        if quantity >= 0:
            total = quantity * price_5
            print(f"Tổng bạn phải trả là: {total}$")
if choice not in list:
    print("Không có trong danh sách")


# Cách 2: Dùng if, else
choice = input("Hãy nhập loại nước trái cây bạn muốn: ").lower()
if choice in list:
    if choice == "cam":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_1
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "táo":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_2
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "xoài":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_3
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "chuối":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_4
            print(f"Tổng bạn phải trả là: {total}$")
    if choice == "nho":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_5
            print(f"Tổng bạn phải trả là: {total}$")
else:
    print("Không có trong danh sách")


# Cách 3: Dùng if, elif, else
choice = input("Hãy nhập loại nước trái cây bạn muốn: ").lower()
if choice in list:
    if choice == "cam":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_1
            print(f"Tổng bạn phải trả là: {total}$")
    elif choice == "táo":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_2
            print(f"Tổng bạn phải trả là: {total}$")
    elif choice == "xoài":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_3
            print(f"Tổng bạn phải trả là: {total}$")
    elif choice == "chuối":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_4
            print(f"Tổng bạn phải trả là: {total}$")
    elif choice == "nho":
        quantity = int(input(f"Nhập số lượng bạn muốn mua: "))
        if quantity < 0:
            print("Số không phù hợp")
        else:
            total = quantity * price_5
            print(f"Tổng bạn phải trả là: {total}$")
else:
    print("Không có trong danh sách")


















































