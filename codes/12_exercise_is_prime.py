import math

def is_prime(n):
    if n == 1:
        return False
    
    flag = True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False

def get_primes(N):
    result = []
    for i in range(1, N + 1):
        if is_prime(i):
            result.append(i)

    return result




print(get_primes(1))
print(get_primes(20))
print(get_primes(100))













