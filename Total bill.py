def Total_Bill(Bill_amount,Tip_perc):
    Total=Bill_amount * (1+0.01*Tip_perc)
    Total=round(Total,2)
    print("Please pay",Total)

Total_Bill(95,10.53)

#to cube

def Cubed_num(num):
    return num*num*num

def Div_3(num1):
    if num1 % 3 ==0:
        return Cubed_num(num1)
    else:
        return False

print(Div_3(90))
print(Div_3(12))
print(Div_3(26))
print(Div_3(51))