arData = []
#100~1까지 list에 넣고 출력
'''
for i in range(100):
    arData.append(100 - i)
print(arData)

'''

#1~100까지 중 짝수만 list에 넣고 출력
'''
for i in range(50):
    arData.append((i+1)*2)
print(arData)

'''

#1~n까지 넣고 n까지의 합 출력
'''
n = int(input("정수를 입력하세요: "))
sum = 0
for i in range(n):
       arData.append(i+1)
       sum += (i+1)
print(sum)

'''
        
#A~F까지 넣고 출력
'''
for i in range(6):
    arData.append(chr(i+65))
print(arData)

'''
#A~F까지중 C제외하고 넣고 출력
'''
arData = ['']*5
for i in range(len(arData)):
    temp = i
    if i > 1:
        temp += 1
    arData[i] = chr(temp+65)

print(arData)

'''
#012012012넣고 출력
'''
arData = [0]*9
for i in range(len(arData)):
   arData[i] = i%3
print(arData)

'''

#정수를 한글로 바꾸기
#예)1024 --> 일공이사
'''
num = int(input("정수 : "))
hangle = "공일이삼사오육칠팔구"
result = ""
while num != 0:
    result = hangle[num%10] + result
    num //= 10
print(result)

'''

'''
data = input("정수 : ")
hangle = "공일이삼사오육칠팔구"
result = ""
for i in data:
    result += hangle[int(i)]
print(result)

'''
#소문자를 대문자로 바꾸기
#예)aPPle1234!@#$ --> APPLE1234!@#$

data = input("문자열 : ")
result = ""
for i in data:
    if ord(i) >= 97 and ord(i) <= 122:
        result += chr(ord(i)-32)
    else:
        result += i
print(result)
