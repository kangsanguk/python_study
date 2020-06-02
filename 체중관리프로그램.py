def bmi(weight, height):
    check = weight/((0.01*height)**2)
    return check
    
weight, height = input("몸무게(kg)와 키(cm) 입력: ").split()
weight = float(weight)
height = float(height)
check = bmi(weight, height)
if (check >= 20.0 and check < 25.0):
    print("표준입니다")
else:
    print("체중관리가 필요합니다")
