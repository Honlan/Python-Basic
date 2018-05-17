numbers = input('Please input a lots of numbers: ')
count1 = {}
count2 = {}
count2['oushu'] = 0
count2['jishu'] = 0

for c in numbers:
    if c in count1:
        count1[c] += 1
    else:
        count1[c] = 1

    if int(c) % 2 == 0:
        count2['oushu'] += 1
    else:
        count2['jishu'] += 1

print(count1)
print(count2)

