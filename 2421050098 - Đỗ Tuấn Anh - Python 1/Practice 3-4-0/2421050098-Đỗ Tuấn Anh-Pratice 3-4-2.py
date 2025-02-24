# Xây dựng chương trình in ra các số từ 10 đến 100



# Cách 1
for i in range(10, 100 + 1):
    if i % 2 == 0:
        print(f"Đây là số chẵn thứ {i}")

# Cách 2
for i in range(10, 100 + 1, 2):
    print(f"Đây là số chẵn thứ {i}")