Medical_cause=(input("Do you have a medical cause?(Y/N)")).strip().upper()

if Medical_cause=="Y":
    print("You are allowed.")
    print("medical cause:", Medical_cause)
else:
    atten=int(input("Enter the attendance of the student."))
    if atten >= 75: 
        print("You are allowed.")
    
    else:
        print("You are not allowed.")



#Electricity Bill

units=int(input("Enter the number of units you have consumed:"))

amount=0
tax=0

if (units < 50 ):
    amount= units * 2.60
    tax=25
elif (units >=50 and units <= 100 ):
    amount=130+(units - 50)* 3.25
    tax=35
elif (units >100 and units <= 200 ):
    amount=130+162.50+(units - 100)* 5.26
    tax=45
elif (units > 200 ):
    amount=130+162.50+526+(units - 200)* 8.45
    tax=75

Total=amount+tax
print("Electricity Bill is :", Total)