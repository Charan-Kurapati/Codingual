num=int(input("Enter a number here:"))

for i in range(1,num+1):
    print(" " * (num-i),end="")
    print("*"*i)