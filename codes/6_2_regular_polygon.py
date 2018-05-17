n = int(input("Please input the edges: "))
import turtle

t = turtle.Turtle()

for i in range(n):
    t.forward(50)
    # t.left(360 / n)
    t.left(180 - 180 * (n - 2) / n)
    
