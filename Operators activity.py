v=10
w=6
x=2
y=2
z=(v+w)*x/y

print("Value of expression is:",z)


# divisibility
print("Enter a number:numerator")
num1=int(input())
print("Enter a number:denominator")
num2=int(input())

if num1%num2==0:
    print(str(num1)+"is divisible by"+str(num2) )

else:
    print(str(num1)+"is not divisible by"+str(num2))


#average

mean1 = 38

wrong_number=36

correct_number=56

total_number=40

#sum of 40 numbers

sum = mean1*total_number

print("the sum of 40 number: ",sum)

#correct sum of these numbers

num2=sum-((wrong_number)+(correct_number))

print("sum-((wrong_number)-(correct_number)): ",num2)

#the correct mean

mean2=num2/total_number

print(mean2)


mean1 = 38

wrong_number=36

correct_number=56

total_number=40

#sum of 40 numbers

sum = mean1*total_number

print("the sum of 40 number: ",sum)

#correct sum of these numbers

num2=sum-wrong_number+correct_number

print("sum-wrong_number+correct_number): ",num2)

#the correct mean

mean2=num2/total_number

print(mean2)



a = int(input("enter a value: "))

b = int(input("enter value 2 :"))

c = int(input("enter value 3: "))

avg = (a + b + c) / 3

print("avg =", avg)

if avg > a and avg > b and avg > c:

    print("%d is higher than %d, %d, %d" %(avg, a, b, c))

elif avg > a and avg > b:

    print("%d is higher than %d, %d" %(avg, a, b))

elif avg > a and avg > c:

    print("%d is higher than %d, %d" %(avg, a, c))

elif avg > b and avg > c:

    print("%d is higher than %d, %d" %(avg, b, c))

elif avg > a:

    print("%d is just higher than %d" %(avg, a))

elif avg > b:

    print("%d is just higher than %d" %(avg, b))

elif avg > c:

    print("%d is just higher than %d" %(avg, c))

else:

    print("invalid input")