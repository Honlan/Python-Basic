count = 0
s = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    count = count + 1
    s = s + value
average = s / count
print('Average: ', average)
