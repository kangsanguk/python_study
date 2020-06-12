def toliter(gallon):
    value = round(gallon*3.785,2)
    print("%.2f 갤론 == %.2f 리터" %(gallon, value))

def togallon(liter):
    value = round(liter*0.264,2)
    print("%.2f 리터 == %.2f 갤론" %(liter, value))

while(True):
    n = int(input("번호 선택 1. 갤론 => 리터 2. 리터 => 갤론 >> "))
    if n == 1:
        a = float(input("변환할 갤론은? "))
        toliter(a)
        break;
    elif n == 2:
        b = float(input("변환할 리터는? "))
        togallon(b)
        break;
    else :
        print("다시 입력해주세요!")
