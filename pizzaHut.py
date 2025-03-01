print("Welcome to pizzaHut Deliveries!")
size=input("What sizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza?Y/N: ").lower()
cheese=input("Do you want extra cheese?Y/N: ").lower()

bill=0
if size == "s":
    bill += 150
elif size == "m":
    bill += 200
elif size == "l":
    bill += 250
else:
    print("You typed wrong input")

if pepperoni == "y":
    if size=="s":
        bill += 20
    else:
        bill += 30    
if cheese == "y":
    bill += 10
print(f"Your final bill is: ₹{bill}. ")    


