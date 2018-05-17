first = 1
second = 1
print(first)
print(second)
turn = 28
while True:
    third =first + second
    print(third)
    first = second
    second = third
    turn -= 1
    if turn == 0:
        break
