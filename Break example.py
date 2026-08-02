word=str(input("Enter a word here:"))

for i in word:
    if i=="A":
        print("A is found.")
        break

    else:
        print("A is not found.")

#Divisiblity checker 

for x in range(50):
    if x % 20==0:
        print("Twist")
    elif x % 15==0:
        pass
    elif x% 5==0:
        print("Fizz")
    elif x % 3==0:
        print("Buzz")
    else:
        print(x)