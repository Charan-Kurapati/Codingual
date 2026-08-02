try:
    age=int(input("Enter your age:"))
    if age <= 0:
        print("Your age is invalid.")
    else:
        print("Your age is:",age)
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    print("INVALID INPUT.Enter a valid number.")