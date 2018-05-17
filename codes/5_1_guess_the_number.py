import random
print("The number is between 0 and 100")
answer = random.randrange(0, 101)
count = 0

while True:
    count += 1
    
    n = int(input("Input the number: "))
    if n > answer:
        print('too big')
    elif n < answer:
        print('too small')
    else:
        print('ok', answer, count)
        break
