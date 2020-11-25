import math
count = 2
i = 5
while(True):
    a = int(math.sqrt(i))
    c = 0
    for b in range (2, a+1):
        if i%b == 0:
            c += 1
    if c == 0:
        count += 1
        if count == 10001:
            print(i)
            break
    i+=1
