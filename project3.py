n = 600851475143
for i in range(2, n+1):
    if n % i == 0:
        n /= i
        print(i)
