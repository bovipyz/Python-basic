# Viết chương trình cho phép nhập thông tin về giới tính, tuổi, năm kinh nghiệm, chiều cao, cân nặng của một người.
# Viết chương trình kiểm tra xem người đó có đủ tiêu chuẩn làm việc trong công ty hay không (tiêu chuẩn đạt ở trong máy tính).






gender = input("Nhập giới tính của bạn: ").lower()
age = int(input("Nhập tuổi của bạn: "))
experience = float(input("Nhập số năm kinh nghiệm của bạn: "))
height = int(input("Nhập chiều cao (cm) của bạn: "))
weight = float(input("Nhập cân nặng (kg) của bạn: "))
meter = height / 100


# Cách 1: Dùng if
# Nữ
if gender == "women" or gender == "female" or gender == "nữ":
    if 30 < age <= 40:
        if experience >= 2:
            if meter >= 1.6:
                if weight >= 50:
                    print("Bạn đã đạt yêu cầu")
                if weight < 50:
                    print("Bạn không đạt cân nặng yêu cầu")
            if meter < 1.6:
                print("Bạn không đạt chiều cao yêu cầu")
        if experience < 2:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")

    if 40 < age <= 60:
        if experience >= 5:
            if meter >= 1.55:
                if weight <= 45:
                    print("Bạn đã đạt yêu cầu")
                if weight > 45:
                    print("Bạn không đạt cân nặng yêu cầu")
            if meter < 1.55:
                print("Bạn không đạt chiều cao yêu cầu ")
        if experience < 5:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")                  
    if 18 <= age <= 30:
        if meter >= 1.55:
            if weight <= 45:
                print("Bạn đã đạt yêu cầu")
            if weight > 45:
                print("Bạn không đạt cân nặng yêu cầu")
        if meter < 1.55:
                print("Bạn không đạt chiều cao yêu cầu")
    if age < 18 or age > 60:
        print("Bạn không đủ tuổi")
# Nam
if gender == "men" or gender == "male" or gender == "nam":
    if 30 < age <= 40:
        if experience >= 2:
            if experience < 2:
                print("Bạn không đạt số năm kinh nghiệm yêu cầu")
            if meter >= 1.7:
                if weight >= 55:
                    print("Bạn đã đạt yêu cầu")
                if weight < 55:
                    print("Bạn không đạt cân nặng yêu cầu")
            if meter < 1.7:
                print("Bạn không đạt chiều cao yêu cầu ") 
        if experience < 2:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
    if 40 < age <= 60:
        if experience < 5:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
        if experience >= 5:
            if meter < 1.6:
                print("Bạn không đạt chiều cao yêu cầu ")  
            if meter >= 1.6:
                if weight <= 54:
                    print("Bạn đã đạt yêu cầu")  
                if weight > 54:
                    print("Bạn không đạt cân nặng yêu cầu")                
    if 18 <= age <= 30:
        if meter < 1.75:
            print("Bạn không đạt chiều cao yêu cầu ")
        if meter >= 1.75:
            if weight < 60:
                print("Bạn không đạt cân nặng yêu cầu")
            if weight >= 60:
                print("Bạn đã đạt yêu cầu")
    if age < 18 or age > 60:
        print("Bạn không đủ tuổi")


# Cách 2: Dùng if, else
# Nữ
if gender == "women" or gender == "female" or gender == "nữ":
    if 30 < age <= 40:
        if experience >= 2:
            if meter >= 1.6:
                if weight >= 50:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu")
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")

    if 40 < age <= 60:
        if experience >= 5:
            if meter >= 1.55:
                if weight <= 45:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu ")
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")                  
    if 18 <= age <= 30:
        if meter >= 1.55:
            if weight <= 45:
                print("Bạn đã đạt yêu cầu")
            else:
                    print("Bạn không đạt cân nặng yêu cầu")
        else:
                print("Bạn không đạt chiều cao yêu cầu")
    if age < 18 or age > 60:
        print("Bạn không đủ tuổi")
# Nam
if gender == "men" or gender == "male" or gender == "nam":
    if 30 < age <= 40:
        if experience >= 2:
            if meter >= 1.7:
                if weight >= 55:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu ") 
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
    if 40 < age <= 60:
        if experience < 5:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
        else:
            if meter < 1.6:
                print("Bạn không đạt chiều cao yêu cầu ")  
            else:
                if weight <= 54:
                    print("Bạn đã đạt yêu cầu")  
                else:
                    print("Bạn không đạt cân nặng yêu cầu")                
    if 18 <= age <= 30:
        if meter < 1.75:
            print("Bạn không đạt chiều cao yêu cầu ")
        else:
            if weight < 60:
                print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn đã đạt yêu cầu")
    if age < 18 or age > 60:
        print("Bạn không đủ tuổi")


# Cách 3: Dùng if, elif, else
# Nữ
if gender == "women" or gender == "female" or gender == "nữ":
    if 30 < age <= 40:
        if experience >= 2:
            if meter >= 1.6:
                if weight >= 50:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu")
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")

    elif 40 < age <= 60:
        if experience >= 5:
            if meter >= 1.55:
                if weight <= 45:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu ")
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")                  
    elif 18 <= age <= 30:
        if meter >= 1.55:
            if weight <= 45:
                print("Bạn đã đạt yêu cầu")
            else:
                    print("Bạn không đạt cân nặng yêu cầu")
        else:
                print("Bạn không đạt chiều cao yêu cầu")
    else:
        print("Bạn không đủ tuổi")
# Nam
if gender == "men" or gender == "male" or gender == "nam":
    if 30 < age <= 40:
        if experience >= 2:
            if meter >= 1.7:
                if weight >= 55:
                    print("Bạn đã đạt yêu cầu")
                else:
                    print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn không đạt chiều cao yêu cầu ") 
        else:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
    elif 40 < age <= 60:
        if experience < 5:
            print("Bạn không đạt số năm kinh nghiệm yêu cầu")
        else:
            if meter < 1.6:
                print("Bạn không đạt chiều cao yêu cầu ")  
            else:
                if weight <= 54:
                    print("Bạn đã đạt yêu cầu")  
                else:
                    print("Bạn không đạt cân nặng yêu cầu")                
    elif 18 <= age <= 30:
        if meter < 1.75:
            print("Bạn không đạt chiều cao yêu cầu ")
        else:
            if weight < 60:
                print("Bạn không đạt cân nặng yêu cầu")
            else:
                print("Bạn đã đạt yêu cầu")
    else:
        print("Bạn không đủ tuổi")
























































































