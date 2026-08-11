#Movie Ticket Booking Summary

name=input("Customer name:")
age=int(input("Age:"))
Ticket=int(input("Number of tickets:"))
if age<=11:
    price=120
elif age<=59:
    price=200
else:
    price=150
amount=price*Ticket
print("Customer Name: ",name)
print("Ticket Price: ₹ ",price)
print("Number of Tickets: ",Ticket)
print("Total Before Discount: ₹ ",amount)
if Ticket>=5:
    discount=0.10*amount
    amount=amount-discount
    print("Discount: ₹ ",round(discount))
    print("Total Amount: ₹ ",round(amount))
else:
    discount=0
    print("Discount: ₹ ",round(discount))
    print("Total Amount: ₹ ",round(amount))