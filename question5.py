#Bus Seat Availability Manager

seats=[ "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"]
for i in range(len(seats)):
    print(f"Seat {i+1}: {seats[i]}")
while True:
    seat=int(input("Enter Seat: "))
    if seats[seat-1]=="Available":
        print(f"Seat booked Successfully.")
        seats[seat-1]="Booked"
        break
    else:
        print(f"Seat is booked, select available seat")
print(f"Total Seats: {len(seats)}")
print(f"Booked Seats: {seats.count("Booked")}")
print(f"Available Seats: {seats.count("Available")}")


    