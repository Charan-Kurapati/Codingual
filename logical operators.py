a=8
b=39
c=68

if a > 0 and b > 0:
    print("They are positive")
elif b > 0 and c > 0:
    print("They are negative")
elif b!=c:
    print("They are not equal to each other")


#BMI checker

height=float(input("Enter your height in centimeters:"))
weight=float(input("Enter your weight in kilograms:"))

BMI = weight / (height/100)**2
print("Your BMI is:",BMI)

if BMI<=18.4:  
    print("You are under weight.")
elif BMI<=24.9:
    print("You are healthy!")
elif BMI<=29.9:
    print("You are overweight.")
elif BMI<=34.9:
    print("You are severely overweight.")
elif BMI<=39.9:
    print("You are obese.")
else:
    print("You are severely obese.")