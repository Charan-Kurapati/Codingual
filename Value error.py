try:
    age=int(input("Enter the age:"))
    if age < 18:
        raise ValueError
    else:
        print("Age is valid.")

except ValueError:
    print("Age is not valid")

#Finally statement

try:
    num1,num2=eval(input("Enter 2 number separated by a comma:"))
    result=num1/num2
    print("Result is:",result)

except ZeroDivisionError:
    print("Division by Zero is error!!")

except SyntaxError:
    print("Comma is missing.Enter numbers separated by comma like 1,2.")

except:
    print("Wrong input.")

else:
    print("No exceptions.")

finally:
    print("The code will execute no matter what!!")