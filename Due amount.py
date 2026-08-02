bill_amount=float(input("Enter bill amount:"))
amount_paid=float(input("Enter amount paid:"))
due_amount=bill_amount-amount_paid

if due_amount > 0:
    print(f"Amount still due £{due_amount:.2f}")
elif due_amount==0:
    print("The full amount has been paid.")
else:
    print(f"Change to return £{abs(due_amount):.2f}")