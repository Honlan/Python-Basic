score = int(float(input("Please input an integer:")))
print(score)

if score > 100 or score < 0:
    print("Wrong Score")
elif score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Medium")
elif score >= 60:
    print("Passed")
else:
    print("Failed")
    
