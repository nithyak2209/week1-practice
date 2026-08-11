#Parking fee calculator

hours=float(input("Enter parking hours:  "))
if hours<=2:
    fee=hours*30
elif hours<=5:
    fee=hours*25
else:
    fee=hours*20
if fee>150:
    service=20
else:
    service=0
print("Parking Charge: ₹ ",round(fee))
print("Service Charge: ₹ ",round(service))
print("Final Amount: ₹ ",round(fee+service))