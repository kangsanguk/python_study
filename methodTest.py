#f(x) = 2x + 1
'''
def f(x):
        return 2*x + 1

result = f(1) + 4
print(result)

'''

#1~10까지의 합을 구해주는 메소드
def sumFrom1To10():
    result = 0
    for i in range(10):
        result += i+1
    print(result)

sumFrom1To10()
