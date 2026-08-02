num=int(input("Enter a decimal number:"))
binary=""
while num > 0:
    reminder = num % 2
    binary = str(reminder) + binary
    num = num // 2
print("Binary number is:",binary)