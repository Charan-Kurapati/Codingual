sum=0
n=int(input("Enter the number whose sum you want to find out:"))

for i in range(1,n+1):
    sum=sum+i
    print("\n sum= ",sum)



#reverse a string

str1=input("Enter any string to reverse it:")
str2=""

for i in str1:
    str2=i+str2

print("The original string is:",str1)
print("The reverse of the string is:",str2)


#reverse order for numbers

n=int(input("Enter any number GREATER than 1:"))

print("Numbers from 0 to 1 are ", format(str(n),str(1)))

for i in range(n,0,-1):
    print(i)