def myFunc(arg1, *arg2):
    if arg1 == '지수':
        print("결과: ", arg2[0], "의", arg2[1],
              "제곱 = ", pow(int(arg2[0]), int(arg2[1])))
    elif arg1 == '최대값':
        max = 0
        for i in range(len(arg2)):
            if int(max) < int(arg2[i]):
                max = arg2[i]
        print("결과:", ",".join(arg2), "의 최대값 =", max)
    elif arg1 == '절대값':
        a = abs(int(arg2[0]))
        print("결과:", arg2[0], "의 절대값 =", a)
    elif arg1 == '평균':
        sum = 0
        for i in range(len(arg2)):
            sum += int(arg2[i])
        a = float(sum / len(arg2))
        print("결과:", ", ".join(arg2), "의 평균 =", a)
    elif arg1 == '정렬':
        a = list(arg2)
        a.sort()
        print("결과:", ", ".join(arg2), "의 정렬결과 =", ", ".join(a))

for i in range(3):
    arg2 = []
    arg1, *arg2 = input("연산자와 값을 입력하시오: ").split()
    if arg1 == '계산기':
        print("결과: " + arg2[0] + " 계산 결과 = " + str(eval(arg2[0])))
    else:
        myFunc(arg1, *arg2)
