print('Question 1')
a = int(input('Number A: '))
b = int(input('Number B: '))
c = int(input('Number C: '))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)


print('Question 2')
s = 0
for i in range(1, 100):
    if i % 2 == 1:
        s = s + i
    else:
        s = s - i
print(s)


print('Question 3')
number = input('A five digit number: ')
if number[::-1] == number:
    print('Yes')
else:
    print('No')


print('Question 4')
import math

n = 1
while True:
    n1 = n + 100
    n2 = n1 + 168

    n1 = math.sqrt(n1)
    n2 = math.sqrt(n2)

    if int(n1) == n1 and int(n2) == n2:
        print(n)
        break
    
    n = n + 1


print('Question 5')
result = 0
for number in range(1, 21):
    s = 1
    for n in range(1, number + 1):
        s = s * n
    result = result + s
print(result)


print('Question 6')
import turtle
t = turtle.Turtle()

t.color('red')
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)
t.forward(100)
t.left(90)
for i in range(3):
    t.forward(200)
    t.left(90)
t.forward(100 + 150)
t.right(90)
t.forward(50)
t.right(90)
t.forward(300)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.penup()
t.goto(25, 100)
t.pendown()
t.seth(90)
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
