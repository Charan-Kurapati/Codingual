n=int(input("Enter number Number:"))
m=int(input("Enter number Power:"))

result =1

for i in range(m):
    result = result * n
    print("Result: ", result)

print(str(n) + " to the power of "+ str(m) +" is: ",result)