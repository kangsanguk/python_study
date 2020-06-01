'''
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
'''
n = 2520
while(True):
    num = 2
    while(num <= 20):
        if n % num != 0:
            n += 1
            check = 0
            break
        num += 1
        check = 1
    if check == 1:
        print(n)
        break
