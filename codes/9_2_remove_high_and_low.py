numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    
# average = (sum(numlist) - max(numlist) - min(numlist)) / (len(numlist) - 2)

# numlist.remove(max(numlist))
# numlist.remove(min(numlist))
# average = sum(numlist) / len(numlist)

# numlist.sort()
# numlist = numlist[1:-1]
# average = sum(numlist) / len(numlist)

print('Average: ', average)

