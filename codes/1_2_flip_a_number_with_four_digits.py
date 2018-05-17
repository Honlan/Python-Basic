# flip a number of four digits
num = 1234
n0 = num % 10
num = (num - n0) / 10
n1 = num % 10
num = (num - n1) / 10
n2 = num % 10
num = (num - n2) / 10
n3 = num % 10
num = (num - n3) / 10
num = n0 * 1000 + n1 * 100 + n2 * 10 + n3 * 1
print(num)
