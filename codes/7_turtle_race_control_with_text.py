import turtle
import random
import time

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-200, 150)
for i in range(21):
    t.write(i)
    t.right(90)
    t.pendown()
    t.forward(300)
    t.penup()
    t.backward(300)
    t.left(90)
    t.forward(20)

alice = turtle.Turtle()
alice.shape('turtle')
alice.color('red')
alice.penup()
alice.goto(-220, 100)

ben = turtle.Turtle()
ben.shape('turtle')
ben.color('blue')
ben.penup()
ben.goto(-220, 0)

claire = turtle.Turtle()
claire.shape('turtle')
claire.color('green')
claire.penup()
claire.goto(-220, -100)

global max_speed_a, max_speed_b, max_speed_c, terminal, order
max_speed_a = 10
max_speed_b = 10
max_speed_c = 10
terminal = 200
order = 0

def key_a():
    global max_speed_a, max_speed_b, max_speed_c, terminal, order
    alice.forward(random.randrange(max_speed_a))
    if alice.xcor() >= terminal and max_speed_a > 1:
        max_speed_a = 1
        t.goto(240, 90)
        if order == 0:
            t.write('冠军', font=('Arial', 20, 'normal'))
        elif order == 1:
            t.write('亚军', font=('Arial', 20, 'normal'))
        elif order == 2:
            t.write('季军', font=('Arial', 20, 'normal'))
        order = order + 1

def key_b():
    global max_speed_a, max_speed_b, max_speed_c, terminal, order
    ben.forward(random.randrange(max_speed_b))
    if ben.xcor() >= terminal and max_speed_b > 1:
        max_speed_b = 1
        t.goto(240, -10)
        if order == 0:
            t.write('冠军', font=('Arial', 20, 'normal'))
        elif order == 1:
            t.write('亚军', font=('Arial', 20, 'normal'))
        elif order == 2:
            t.write('季军', font=('Arial', 20, 'normal'))
        order = order + 1

def key_c():
    global max_speed_a, max_speed_b, max_speed_c, terminal, order
    claire.forward(random.randrange(max_speed_c))
    if claire.xcor() >= terminal and max_speed_c > 1:
        max_speed_c = 1
        t.goto(240, -110)
        if order == 0:
            t.write('冠军', font=('Arial', 20, 'normal'))
        elif order == 1:
            t.write('亚军', font=('Arial', 20, 'normal'))
        elif order == 2:
            t.write('季军', font=('Arial', 20, 'normal'))
        order = order + 1

s = turtle.Screen()
s.onkey(key_a, 'a')
s.onkey(key_b, 'b')
s.onkey(key_c, 'c')
s.listen()


