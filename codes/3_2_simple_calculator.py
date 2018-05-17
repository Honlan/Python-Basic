error = False

try:
    num1 = float(input("the first number: "))
except:
    print("Please input a number")
    error = True
try:
    num2 = float(input("the second number: "))
except:
    print("Please input a number")
    error = True

op = input("the operator(+ - * / **):")

if error:
    print("Something Wrong")
else:
    if num2 == 0 and op == '/':
        print("The division can't be 0")
    elif op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '**':
        print(num1 ** num2)
    else:
        print("Unknown Operator")
