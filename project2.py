a = 1
b = 2
sum = 2
while(True):
    a0 = a + b
    if a0 > 4000000:
        break
    a = a0
    if a % 2 == 0:
        sum += a
    b0 = a + b
    if b0 > 4000000:
        break
    b = b0
    if b % 2 == 0:
        sum += b
    
print(sum)
