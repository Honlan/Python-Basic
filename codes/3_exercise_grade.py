score = int(float(input("Please input an integer:")))
print(score)

if score > 100:
    print("Wrong Score")
elif score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Medium")
elif score >= 60:
    print("Passed")
elif score >= 0:
    print("Failed")
else:
    print("Wrong Score")
    
