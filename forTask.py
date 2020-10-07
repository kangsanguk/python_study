#100~1까지 출력
'''
for i in range(0, 100, 1):
    print(100 - i)

'''

#100~1까지중 짝수만 출력
'''
for i in range(0, 50, 1):
    print(100 - 2*i)

'''

#1~100까지의 합 구하기
'''
sum = 0
for i in range(0, 100, 1):
    sum += (100 - i)
print(sum)

'''

#1~N까지의 합 구하기(N은 사용자에게 입력받는다)
'''
n = int(input("n : "))
sum = 0
if n > 1:
    for i in range(1, n+1, 1):
       sum += i
    print(sum)
else:
    print("1보다 큰값을 입력하세요")
'''


#A~F까지 출력
#chr(정수), ord(문자)
'''
for i in range(6):
    print(chr(i + 65))
'''


#A~F까지 중 C제외하고 출력
'''
for i in range(65, 71, 1):
    if i != 67:
        print("%c" %i)
'''


#aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력

for i in range(65, 91, 1):
    if i % 2 == 0:
        print("%c" %i, end = '')
    else:
        print("%c" %(i+32), end = '')
print()

