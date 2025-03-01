print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=int(input("What percentage tip would you like to give ? 10 , 12 or 15 "))
People=int(input("How many people to split the bill ?"))
tip_as_percentage = tip/100
total_tip_amount = tip_as_percentage*bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / People
final_amount = round(bill_per_person,2)
print("Each person should pay",final_amount)