sum1 = 0
sum2 = 0
for i in range(1, 101):
    sum1 += i*i
    sum2 += i
sum = sum2 * sum2
n = sum - sum1
print(n)
