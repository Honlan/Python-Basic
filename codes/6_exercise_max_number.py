import math
largest_so_far = -math.inf

numbers = [3, 14, -5, 42, 98, 5]
for i in numbers:
    if i > largest_so_far:
        largest_so_far = i
print(largest_so_far)
print(i)
