# from big to small
n = int(input("n: "))
s = 0
while n > 0:
    s = s + n
    n = n - 1
print(s)

# from small to big
n = int(input("n: "))
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print(s)
