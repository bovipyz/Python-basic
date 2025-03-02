# In danh sách đồ uống ra màn hình
# In danh sách đồ uống và giá tiền của nó ra màn hình


juices_name = ["táo", "xoài", "chuối"]
print(f"Danh sách đồ uống: {juices_name}")

juices_menu = ["táo", "xoài", "chuối", 10, 20, 30]
print("Danh sách đồ uống nước trái cây:")
for i in range(3):
    print(f"{juices_menu[i]} : {juices_menu[i+3]}")