a = 1
total = 0
while True:
    total += a
    a += 1
    count = 0
    for i in range (1, total+1):
        if total % i == 0:
            count += 1
    if count>= 500:
        print(total)
        break
    print(total)
