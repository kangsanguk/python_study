#자동 형변환
print(10//3)
print(10.0//3)
print("-----------------------------------")

#강제 형변환
print(float(10)//3)

#문자 형변환
#ord(문자) : 문자를 아스키 코드로
#chr(정수) : 정수를 문자로
#data = 'ABC'
#print("%c" %67)
'''
pw = "a1b2c3"
en_pw = ""

for i in pw:
    en_pw += chr(ord(i) * 3)

print("암호 : %s" %pw)
print("암호화 : %s" %en_pw)
'''

#문자열
data = '123'
print(type(data))

#연결과 연산
#연결 str + str
#연산 num + num
print(int(data) + 3)
print(data + '3')

name = "강상욱"
print("이름 : " + name)
