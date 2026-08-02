num1=int(input("Enter your first number here:"))
num2=int(input("Enter your second number here:"))
def add(num1,num2):
    result=num1+num2
    print("The 2 numbers together are:",result)
add(num1,num2)
def sub(num1,num2):
    result=num1-num2
    print("The 2 numbers subtracted are:",result)
sub(num1,num2)
def times(num1,num2):
    result=num1*num2
    print("The 2 numbers multiplied are:",result)
times(num1,num2)
def divide(num1,num2):
    result=num1/num2
    print("The 2 numbers divided are:",result)

try:
    divide(num1,num2)
    if num2==0:
        raise ZeroDivisionError
    else:
        print("Number is valid")
except ZeroDivisionError:
    print("You cannot divide by ZERO!")