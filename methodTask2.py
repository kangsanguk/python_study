#5개의 정수를 입력받고 최대값과 최소값을 구해주는 메소드
'''
Max = 0
Min = 0
def MaxMin(Max, Min, num):
    if num >= Max:
        Max = num
    if Min >= num:
        Min = num
    return Max, Min
for i in range(5):
            num = int(input("정수를 입력: "))
            MaxMin(Max, Min, num)
            print("최대값 : %d, 최소값 : %d" %(Max, Min))

print("최대값 : %d, 최소값 : %d" %(Max, Min))

'''
'''
def MaxMin(arData):
    Max = arData[0]
    Min = arData[0]

    for i in range(1, len(arData)):
        if Max < arData[i]:
            Max = arData[i]
        if Min > arData[i]:
            Min = arData[i]

    return Max, Min

arData = [1, 5, 3, 9, 5]
result = MaxMin(arData)
print("최대값 : %d, 최소값 : %d" %(result[0], result[1]))

'''

#소문자를 대문자로 바꿔주는 메소드
#aPPle1234!@#$ >>> APPLE1234!@#$
'''
def Upper(string):
    result = ''
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

print(Upper("aPPle1234!@#$"))

'''

#한글을 정수로 바꿔주는 메소드
#예)일공이사 >>> 1024

def Hangle(hangle):
    hangle_org = "공일이삼사오육칠팔구"
    result = ''
    for i in hangle:
        result += str(hangle_org.index(i))

    result = int(result)
    return result

result = Hangle("일공이사")
print(result)














