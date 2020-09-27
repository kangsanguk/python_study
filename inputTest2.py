#두 정수의 합

'''
n1Msg = "첫번째 정수 : "
n2Msg = "두번째 정수 : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

result = num1 + num2
print("%d + %d = %d" %(num1, num2, result))

'''


'''
#TV프로그램
#프로그램 이름 :
#프로그램 방영날짜 :
#프로그램 MC :
#시청률 : (실수)%

msg1 = "TV프로그램"
msg2 = "프로그램 이름 : "
msg3 = "프로그램 방영날짜 : "
msg4 = "프로그램 MC : "
msg5 = "시청률 : "

print(msg1)
name = input(msg2)
date = input(msg3)
mc = input(msg4)
watch = float(input(msg5))

print()
print(msg1)
print("%s %s" %(msg2, name))
print("%s %s" %(msg3, date))
print("%s %s" %(msg4, mc))
print("%s %.2f%%" %(msg5, watch))

'''

#split()
#A.b : A안에 b
'''
data1, data2, data3 = "a,b,c".split(',')
print(data1)
print(data2)
print(data3)

'''
'''
msg = "핸드폰 번호를 아래와 같은 양식으로 작성해주세요"\
      + " 010-1234-1234\n"

fNum, sNum, lNum = input(msg).split('-')
print("통신사 번호 : " +fNum)
print("중간 번호 : %s" %sNum)
print("마지막  번호 : " +lNum)
'''


'''
#split()은 값이 없어도 체크할 수 있기 때문에
#실무에서 자주 사용된다.
name, age, gender = input("테스트").split(',')
print(name)
print(age)
print(gender)
'''
print(10&11)
print(10|11)
print(10^11)
print(~10)
print(~-10)










