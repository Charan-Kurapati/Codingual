number=int(input("Enter numbers here:"))
count=0
while number > 0:
    number = number // 10
    count = count + 1
print("The number of digits:",count)