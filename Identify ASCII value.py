value=input("Enter ONE character:")

if len(value) == 1:

    val=ord(value)
    print("The ASCII value of " + value + " is: ", val)
    if value.isupper():
        print("The value is UPPER CASE.")
    elif value.islower():
        print("The value is LOWER CASE.")
    elif value.isdigit():
        print("The value is a DIGIT")
    else:
        print("The value is a SPECIAL.")
else:
    print("Enter only ONE character.")