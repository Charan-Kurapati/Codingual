n=int(input("Enter the number of terms:"))

sum=0

i=1
while  (i<=n):
    sum=sum+i
    i=i+1

print(sum)


#infinite loop

i=0

while i<=0:
    print("I WILL RUN FOREVER!!!")


#armstrong number

num=int(input("Enter any number over 1 digit:"))

sum=0

temp=num
power=temp%10
while temp>0:
    digit=temp%10
    sum=sum+digit**power
    temp=temp//10

print("sum",sum)

if num==sum:
    print(num,"is a armstrong number.")
else:
    print(num,"is not a armstrong number.")