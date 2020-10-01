#대소비교
#두 정수 입력받기

msg1 = "첫번째 정수 : "
msg2 = "두번째 정수 : "

num1 = int(input(msg1))
num2 = int(input(msg2))

'''
print("큰 값 : %d" %num1) if num1 > num2 else \
         print("두 수가 같습니다") if num1 == num2 else print("큰 값 : %d" %num2)

'''

result = num1 if num1 > num2 else \
         'equals' if num1 == num2 else num2

msg = "두 수가 같습니다" if result == 'equals' else "큰 값 : " + str(result)

print(msg)
