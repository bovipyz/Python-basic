# Cho phép sinh viên nhập điểm 3 môn Toán, Lý và Hóa của mình
# Tính tổng điểm của sinh viên, sau đó so sánh với điểm chuẩn của từng ngành
# CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15
# In kết quả xem người dùng đã trúng tuyển vào những ngành nào





print("Điểm chuẩn các ngành: CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15")
math = float(input("Nhập điểm môn toán: "))
physics = float(input("Nhập điểm môn vật lý: "))
chemistry = float(input("Nhập điểm môn hóa: "))



# Cách 1: Dùng if
if math < 0 or physics < 0 or chemistry < 0:
    print("Số không hợp lệ")
if math > 10 or physics > 10 or chemistry > 10:
    print("Số không hợp lệ")
if 0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10:
    total = math + physics + chemistry
    print(f"Tổng điểm xét tuyển: {total} điểm")
    if total >= 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    if 18 <= total < 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    if 17 <= total < 18:
        print("Chúc mừng bạn đã trùng tuyển các ngành: Địa chất: 17; Môi Trường: 15")
    if 15 <= total < 17:
        print("Chúc mừng bạn đã trùng tuyển ngành: Môi Trường: 15")
    if total < 15:
        print("Bạn đã trượt xét tuyển")


# Cách 2: Dùng if, else
if 0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10:
    total = math + physics + chemistry
    print(f"Tổng điểm xét tuyển: {total} điểm")
    if total >= 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    if 18 <= total < 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    if 17 <= total < 18:
        print("Chúc mừng bạn đã trùng tuyển các ngành: Địa chất: 17; Môi Trường: 15")
    if 15 <= total < 17:
        print("Chúc mừng bạn đã trùng tuyển ngành: Môi Trường: 15")
    if total < 15:
        print("Bạn đã trượt xét tuyển")
else:
    print("Số không hợp lệ")


# Cách 3: Dùng if, elif, else:
if 0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10:
    total = math + physics + chemistry
    print(f"Tổng điểm xét tuyển: {total} điểm")
    if total >= 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; CNTT chất lượng cao: 22; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    elif 18 <= total < 22:
        print("Chúc mừng bạn đã trùng tuyển các ngành: CNTT: 18; KHDL: 18; Địa chất: 17; Môi Trường: 15")
    elif 17 <= total < 18:
        print("Chúc mừng bạn đã trùng tuyển các ngành: Địa chất: 17; Môi Trường: 15")
    elif 15 <= total < 17:
        print("Chúc mừng bạn đã trùng tuyển ngành: Môi Trường: 15")
    else:
        print("Bạn đã trượt xét tuyển")
else:
    print("Số không hợp lệ")






    



























































