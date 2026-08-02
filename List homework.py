num=int(input("Enter a number:"))

odd_numbers=[x for x in range(1,num) if x % 2 != 0]
print("Odd numbers:", odd_numbers)


#fruits

fruits=["dragonfruit","grapes","apple","banana","orange"]

cap_fruits=[fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Updated list:", cap_fruits)