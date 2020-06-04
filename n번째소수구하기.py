def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_number_list(length):
    result = []
    n = 2
    while(len(result) <= (length-1)):
        check = is_prime(n)
        if check == True:
            result.append(n)
        n += 1
    return result

length = int(input('Length? '))
print(prime_number_list(length))
