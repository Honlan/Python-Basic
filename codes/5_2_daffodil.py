A = 1
B = 0
C = 0
while True:
    res = 100 * A + 10 * B + C
    if res == A ** 3 + B ** 3 + C ** 3:
        print(res)
    C += 1
    if C == 10:
        C = 0
        B += 1
    if B == 10:
        B = 0
        A += 1
    if A == 10:
        break

n = 100
while n <= 999:
    ans = n
    
    n0 = ans % 10
    ans = (ans - n0) / 10
    n1 = ans % 10
    ans = (ans - n1) / 10
    n2 = ans

    if n0 ** 3 + n1 ** 3 + n2 ** 3 == n:
        print(n)

    n += 1
    
