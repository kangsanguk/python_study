max = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        n = i * k
        n1 = int(str(n)[::-1])
        if n == n1:
            if max < n:
                max = n
print(max)
