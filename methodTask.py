#1~10까지 출력하는 메소드
'''
def print1to10():
    for i in range(10):
        print(i+1, end = '')
    print()

print1to10()

'''

#1~n까지의 합을 구해주는 메소드
'''
def sum1toN():
    sum = 0
    n = int(input("정수입력: "))
    for i in range(n):
        sum += i+1
    print(sum)

sum1to10()

'''

#홀수를 짝수로 짝수를 홀수로 바꿔주는 메소드


def cange(x):
    if x % 2 == 0:
        x += 1
        return x
        print("짝수에서 홀수로 변경되었습니다. %d -> %d" %(temp, x))
    else:
        temp = x
        x += 1
        return x
        print("홀수에서 짝수로 변경되었습니다. %d -> %d" %(temp, x))

cange(3)


#두 정수의 나눗셈 메소드

'''
def div(num1, num2):
    if num2 != 0:
        value = num1 // num2
        rest = num1 % num2
        print("몫 : %d

'''

