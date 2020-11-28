import math

total = 5
for n in range(5, 2000000):
    a = int(math.sqrt(n))
    count=0
    for i in range(2, a+1):
        if n%i==0:
            count+=1
    if count==0:
        total+=n
print(total)
