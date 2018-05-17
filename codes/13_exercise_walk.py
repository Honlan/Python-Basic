def walk(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return walk(N - 1) + walk(N - 2)

print(walk(20))
