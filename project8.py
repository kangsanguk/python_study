import math
for a in range(1, 333):
    for b in range(a+1, 500):
        c = 1000-a-b
        d = pow(a, 2) + pow(b,2)
        if pow(c, 2) == d:
            print(a * b * c)
