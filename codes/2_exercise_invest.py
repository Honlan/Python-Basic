money = float(input("How much money"))
month = float(input("How many months"))
rate = float(input("How much rate"))
rate = rate / 100
total = money * (1 + rate) ** month
interest = total - money
print(interest)
