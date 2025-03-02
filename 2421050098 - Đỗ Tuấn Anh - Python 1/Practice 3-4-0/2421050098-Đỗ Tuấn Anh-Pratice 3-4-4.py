# Tạo một biến kiểu list để lưu tên đồ uống
# Tạo một biến kiểu list để lưu tên giá đồ uống
# In menu ra màn hình 





# Cách 1
juices_menu = ['táo', 'xoài', 'chuối']
juices_price = [10, 20, 30]

for i in range(len(juices_menu)):
    print(juices_menu[i], "--", juices_price[i])

# Cách 2
juices_menu_and_price = ["táo", 10, "xoài", 20, "chuối", 30]
for i in range(0, 5, 2):
    print(juices_menu_and_price[i], "--", juices_menu_and_price[i+1])

# Cách 3
juices_menu_and_price = ["táo", "xoài", "chuối", 10, 20, 30]
for i in range(3):
    print(juices_menu_and_price[i], "--", juices_menu_and_price[i+3])































