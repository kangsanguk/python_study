#대소비교
n1Msg = "첫번째 정수 : "
n2Msg = "두번째 정수 : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

msg = ""

if num1 > num2 : msg = "큰 값 : " + str(num1)
elif num1 < num2 : msg = "큰 값 : " + str(num2)
else : msg = "두 수가 같습니다."

print(msg)
