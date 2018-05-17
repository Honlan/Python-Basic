for N in range(2, 1001):
    f = True
    for i in range(2, N):
        if N % i == 0:
            f = False
            break

    if f:
        print(N, 'is a Prime')
