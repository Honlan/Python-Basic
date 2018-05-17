def fibo(N):
    if N <= 2:
        return 1
    else:
        return fibo(N - 1) + fibo(N - 2)

print(fibo(8))
