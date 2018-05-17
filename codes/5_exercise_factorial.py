# from big to small
n = int(input("n: "))
s = 1
while n > 0:
    s = s * n
    n = n - 1
print(s)

# from small to big
n = int(input("n: "))
i = 1
s = 1
while i <= n:
    s = s * i
    i = i + 1
print(s)
